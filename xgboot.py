import yfinance as yf
import pandas as pd
import torch
import torch.nn as nn


from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report

ticker="AAPL"

df=yf.download(ticker,start="2022-01-01",end="2025-01-01")


df["Return"]=df["close"].pct_change()
df["MA5"]=df["close"].rolling(5).mean()
df["MA10"]=df["close"].rolling(10).mean()
df["MA20"]=df["close"].rolling(20).mean()
df["Volatility"]=df["Return"].rolling(20).std()
df["momentum"]=df["close"]-df["close"].shift(5)
df["target"]=(df["close"].shift(-1)>df["close"]).astype(int)

df.dropna()

features = [
    "Return",
    "MA5",
    "MA10",
    "MA20",
    "Volatility",
    "Momentum",
    "Volume"
]

X=df[features].values
y=df['Target'].values


split_index=int(len(df)*0.8)

X_train=X[:split_index]
X_test=X[split_index:]
y_train=y[:split_index]
y_test=y[split_index:]


scalar=StandardScaler()
X_train=scalar.fit_transform(X_train)
X_test=scalar.transform(X_test)

X_train=torch.tensor(X_train,dtype=torch.float32)
y_train=torch.tensor(y_train,dtype=torch.float32).view(-1,1)
y_test=torch.tensor(y_test,dtype=torch.float32).view(-1,1)
X_test=torch.tensor(X_test,dtype=torch.float32)

print(X_train.shape,X_test.shape)
