"""Look at the last 20 days of stock data and predict the next value."""



import torch.nn as nn
import numpy as np
import torch

X=np.random.rand(200,20,1).astype(np.float32)#200 samples,20 rows,1 column
y=np.random.rand(200,1).astype(np.float32)
X_train = torch.tensor(X)
y_train = torch.tensor(y)

#(200, 20, 1)--(200, 20, 64)-(200, 64)-(200, 1)
class RNNModel(nn.Module):
    def __init__(self):
        self.rnn=nn.RNN(input_size=1,hidden_size=64,num_layers=2,batch_first=True)
        self.fc=nn.Linear(64,1)
    def forward(self,x):
        out,hidden=self.rnn(x)
        out=out[:,-1,:]
        out=self.fc(out)
        return out
    
model=RNNModel()
criterion=nn.MSELoss()
optimizer=torch.optim.AdamW(model.parameters(),lr=1e-4,weight_decay=0.01
                           )
epochs=10
for epoch in range(epochs):
    prediction=model(X_train)
    loss=criterion(prediction,y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")



