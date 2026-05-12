import yfinance as yf
import pandas as pd
import torch
import torch.nn as nn

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

ticker = "AAPL"

df = yf.download(ticker, start="2022-01-01", end="2025-01-01")

df["Return"] = df["Close"].pct_change()
df["MA5"] = df["Close"].rolling(5).mean()
df["MA10"] = df["Close"].rolling(10).mean()
df["MA20"] = df["Close"].rolling(20).mean()
df["Volatility"] = df["Return"].rolling(20).std()
df["Momentum"] = df["Close"] - df["Close"].shift(5)
df["target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

df = df.dropna()

features = [
    "Return",
    "MA5",
    "MA10",
    "MA20",
    "Volatility",
    "Momentum",
    "Volume"
]

X = df[features].values
y = df["target"].values

split_index = int(len(df) * 0.8)

X_train = X[:split_index]
X_test = X[split_index:]
y_train = y[:split_index]
y_test = y[split_index:]

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
y_test = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)
X_test = torch.tensor(X_test, dtype=torch.float32)

print(X_train.shape, X_test.shape)


class StockDirection(nn.Module):
    def __init__(self, input_size):
        super(StockDirection, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.network(x)


model = StockDirection(input_size=len(features))

criterion = nn.BCELoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4, weight_decay=1e-4)

epochs = 100
for epoch in range(epochs):
    model.train()
    output = model(X_train)
    optimizer.zero_grad()
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")


model.eval()
