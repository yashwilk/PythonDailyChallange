import random
import numpy as np
import pandas as pd
from dataclasses import dataclass

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader


@dataclass
class Config:
    n_days: int = 1800
    rows_per_day: int = 50
    n_features: int = 20
    seq_len: int = 20

    batch_size: int = 256
    epochs: int = 5
    lr: float = 1e-3

    hidden_size: int = 64
    num_layers: int = 2
    dropout: float = 0.2

    use_aux_targets: bool = True
    use_online_learning: bool = True

    seed: int = 42
    device: str = "cuda" if torch.cuda.is_available() else "cpu"


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def create_dummy_data(cfg):
    rows = []

    for date_id in range(cfg.n_days):
        base_signal = np.sin(date_id / 30)

        for _ in range(cfg.rows_per_day):
            features = np.random.normal(0, 1, cfg.n_features)

            target = (
                0.3 * features[0]
                - 0.2 * features[1]
                + 0.1 * features[2]
                + base_signal
                + np.random.normal(0, 0.1)
            )

            aux_1 = target + np.random.normal(0, 0.05)
            aux_2 = features[3] * 0.5 + np.random.normal(0, 0.1)

            row = {
                "date_id": date_id,
                "target": target,
                "aux_1": aux_1,
                "aux_2": aux_2,
            }

            for i in range(cfg.n_features):
                row[f"feature_{i}"] = features[i]

            rows.append(row)

    return pd.DataFrame(rows)


class TimeSeriesDataset(Dataset):
    def __init__(self, df, feature_cols, cfg):
        self.df = df.reset_index(drop=True)
        self.feature_cols = feature_cols
        self.cfg = cfg

        self.X = self.df[feature_cols].values.astype(np.float32)
        self.y = self.df["target"].values.astype(np.float32)
        self.aux = self.df[["aux_1", "aux_2"]].values.astype(np.float32)

    def __len__(self):
        return len(self.df) - self.cfg.seq_len

    def __getitem__(self, idx):
        x_seq = self.X[idx : idx + self.cfg.seq_len]
        y = self.y[idx + self.cfg.seq_len]
        aux = self.aux[idx + self.cfg.seq_len]

        return (
            torch.tensor(x_seq),
            torch.tensor(y),
            torch.tensor(aux),
        )


class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, dropout, use_aux_targets):
        super().__init__()

        self.use_aux_targets = use_aux_targets

        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )

        self.target_head = nn.Linear(hidden_size, 1)

        if use_aux_targets:
            self.aux_head = nn.Linear(hidden_size, 2)

    def forward(self, x):
        output, _ = self.lstm(x)
        last_hidden = output[:, -1, :]

        target_pred = self.target_head(last_hidden).squeeze(1)

        if self.use_aux_targets:
            aux_pred = self.aux_head(last_hidden)
            return target_pred, aux_pred

        return target_pred, None


def correlation_score(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if np.std(y_true) == 0 or np.std(y_pred) == 0:
        return 0

    return np.corrcoef(y_true, y_pred)[0, 1]


def train_one_epoch(model, loader, optimizer, cfg):
    model.train()

    mse = nn.MSELoss()
    total_loss = 0

    for x, y, aux in loader:
        x = x.to(cfg.device)
        y = y.to(cfg.device)
        aux = aux.to(cfg.device)

        optimizer.zero_grad()

        target_pred, aux_pred = model(x)

        loss = mse(target_pred, y)

        if cfg.use_aux_targets and aux_pred is not None:
            aux_loss = mse(aux_pred, aux)
            loss = loss + 0.3 * aux_loss

        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    return total_loss / len(loader)


def validate(model, loader, cfg):
    model.eval()

    preds = []
    targets = []

    with torch.no_grad():
        for x, y, aux in loader:
            x = x.to(cfg.device)

            target_pred, _ = model(x)

            preds.extend(target_pred.cpu().numpy())
            targets.extend(y.numpy())

    return correlation_score(targets, preds)


def run_fold(df, cfg, fold_name, valid_start, valid_end):
    feature_cols = [c for c in df.columns if c.startswith("feature_")]

    train_df = df[df["date_id"] < valid_start].copy()
    valid_df = df[(df["date_id"] >= valid_start) & (df["date_id"] <= valid_end)].copy()

    train_dataset = TimeSeriesDataset(train_df, feature_cols, cfg)
    valid_dataset = TimeSeriesDataset(valid_df, feature_cols, cfg)

    train_loader = DataLoader(
        train_dataset,
        batch_size=cfg.batch_size,
        shuffle=True,
        drop_last=True,
    )

    valid_loader = DataLoader(
        valid_dataset,
        batch_size=cfg.batch_size,
        shuffle=False,
    )

    model = LSTMModel(
        input_size=len(feature_cols),
        hidden_size=cfg.hidden_size,
        num_layers=cfg.num_layers,
        dropout=cfg.dropout,
        use_aux_targets=cfg.use_aux_targets,
    ).to(cfg.device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=cfg.lr)

    best_score = -999

    for epoch in range(cfg.epochs):
        train_loss = train_one_epoch(model, train_loader, optimizer, cfg)
        score = validate(model, valid_loader, cfg)

        best_score = max(best_score, score)

        print(
            f"{fold_name} | Epoch {epoch+1} | "
            f"Loss: {train_loss:.5f} | Score: {score:.5f}"
        )

    if cfg.use_online_learning:
        print(f"{fold_name} | Running online learning step...")

        online_dataset = TimeSeriesDataset(valid_df, feature_cols, cfg)
        online_loader = DataLoader(
            online_dataset,
            batch_size=cfg.batch_size,
            shuffle=True,
            drop_last=True,
        )

        train_one_epoch(model, online_loader, optimizer, cfg)

    return best_score


def run_experiment(
    use_aux_targets=True,
    use_online_learning=True,
    seed=42,
):
    cfg = Config(
        use_aux_targets=use_aux_targets,
        use_online_learning=use_online_learning,
        seed=seed,
    )

    set_seed(cfg.seed)

    df = create_dummy_data(cfg)

    folds = {
        "CV fold 0": (1298, 1498),
        "CV fold 1": (1499, 1698),
        "Fold 1 with 200 days gap": (1499, 1698),
    }

    scores = {}

    for fold_name, (valid_start, valid_end) in folds.items():
        if fold_name == "Fold 1 with 200 days gap":
            train_df = df[df["date_id"] < valid_start - 200].copy()
            valid_df = df[
                (df["date_id"] >= valid_start) & (df["date_id"] <= valid_end)
            ].copy()
            temp_df = pd.concat([train_df, valid_df], axis=0)
            score = run_fold(temp_df, cfg, fold_name, valid_start, valid_end)
        else:
            score = run_fold(df, cfg, fold_name, valid_start, valid_end)

        scores[fold_name] = score

    scores["CV avg"] = np.mean(list(scores.values()))

    return scores


if __name__ == "__main__":

    experiments = [
        ("LSTM without both auxiliary targets and online learning", False, False, 42),
        ("LSTM without auxiliary targets", False, True, 42),
        ("LSTM", True, True, 42),
        ("LSTM seed 2", True, True, 123),
    ]

    results = []

    for name, use_aux, use_online, seed in experiments:
        print("\n" + "=" * 80)
        print(name)
        print("=" * 80)

        scores = run_experiment(
            use_aux_targets=use_aux,
            use_online_learning=use_online,
            seed=seed,
        )

        row = {"Model": name}
        row.update(scores)
        results.append(row)

    results_df = pd.DataFrame(results)

    print("\nFinal Scores")
    print(results_df)

    results_df.to_csv("dummy_lstm_scores.csv", index=False)




class TimeSeriesDataset(Dataset):
    def __init__(self, df, feature_cols, cfg):
        self.df = df.reset_index(drop=True)
        self.feature_cols = feature_cols
        self.cfg = cfg

        self.X = self.df[feature_cols].values.astype(np.float32)
        self.y = self.df["target"].values.astype(np.float32)
        self.aux = self.df[["aux_1", "aux_2"]].values.astype(np.float32)

    def __len__(self):
        return len(self.df) - self.cfg.seq_len  
    
    def __getitem__(self, idx):
        x_seq = self.X[idx : idx + self.cfg.seq_len]
        y = self.y[idx + self.cfg.seq_len]
        aux = self.aux[idx + self.cfg.seq_len]

        return (
            torch.tensor(x_seq),
            torch.tensor(y),
            torch.tensor(aux),
        )
    


    class LSTMModel(nn.Module):
        def __init__(self, input_size, hidden_size, num_layers, dropout, use_aux_targets):
            super().__init__()

            self.use_aux_targets = use_aux_targets

            self.lstm = nn.LSTM(
                input_size=input_size,
                hidden_size=hidden_size,
                num_layers=num_layers,
                batch_first=True,
                dropout=dropout,
            )

            self.target_head = nn.Linear(hidden_size, 1)

            if use_aux_targets:
                self.aux_head = nn.Linear(hidden_size, 2)

        def forward(self, x):
            output, _ = self.lstm(x)
            last_hidden = output[:, -1, :]

            target_pred = self.target_head(last_hidden).squeeze(1)

            if self.use_aux_targets:
                aux_pred = self.aux_head(last_hidden)
                return target_pred, aux_pred

            return target_pred, None
        

        def tr