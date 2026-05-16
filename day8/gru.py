import os
import numpy as np
import pandas as pd
import torch
from dataclasses import dataclass
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

try:
    import wandb
    WandB_AVAILABLE = True
except ImportError:
    WandB_AVAILABLE = False



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

    use_wandb: bool = False
    project_name: str = "dummy-gru-experiment"


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    """So even though randomness exists, it becomespredictable randomnessEvery run gets the SAME order.
    Python → shuffle filenames
NumPy → preprocess arrays
PyTorch CPU → create tensors
PyTorch GPU → train neural network"""


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

"""20 feature columns,1 target column,2 auxillary columns,1 date_id column)"""
"""date_id is the day number and it repeates for 50 rows. So we have 1800 days and 50 rows per day. So total 90000 rows. Each row has 20 features,1 target and 2 auxillary columns."""



class TimeSeriesDataset(Dataset):
    def __init__(self,df,feature_cols,cfg):
        self.df=df.reset_index(drop=True)
        self.feature_cols=feature_cols
        self.cfg=cfg

        self.X = self.df[feature_cols].values.astype(np.float32)
        self.y=self.df["target"].values.astype(np.float32)
        self.aux=self.df[["aux_1","aux_2"]]
        def __len__(self):
            return len(self.df)-self.cfg.seq_len
        def __getitem__(self,idx):
            x_seq=self.X[idx:idx+self.cfg.seq_len]#eg 0-50
            y=self.y[idx+self.cfg.seq_len]# 51
            aux=self.aux[idx+self.cfg.seq_len]
            torch.tensor(x_seq)
            return (
            torch.tensor(x_seq),
            torch.tensor(y),
            torch.tensor(aux),
        )


