"""Given an integer array nums and an integer k, return the k most frequent elements.
Input:
nums = [1,1,1,2,2,3]
k = 2

Output:
[1,2]
"""
from collections import Counter
import heapq
import torch


def topkfrequent(nums,k):
    freq=Counter(nums)
    return heapq.nlargest(k,freq.keys(),key=freq.get)


"""How do you detect and remove outliers using the IQR method?"""
import pandas as pd
df = pd.DataFrame({
    "Salary": [30000, 35000, 40000, 45000, 50000, 1000000]
})
Q1=df['Salary'].quantile(0.25)
Q3=df['Salary'].quantile(0.75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
filtered_df=df[(df['Salary']>=lower_bound) & (df['Salary']<=upper_bound)]
print(filtered_df)



"What is Regularization in Machine Learning?"
"Regularization helps prevent overfitting by adding a penalty term to the loss function."
"A loss function is a mathematical function that measures how wrong a machine learning or deep learning model’s predictions are compared to the actual answers."


from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

X,y=make_regression(n_samples=100,n_features=5,noise=10,random_state=42)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=Ridge(alpha=1.0)#alpha controls regularization strength.Ridge uses L2 regularization:"""
model.fit(X_train,y_train)
print("model trained with regularization")#L1 lasso regularization and L2 ridge regularization are two common types of regularization techniques used in machine learning to prevent overfitting. L1 regularization adds a penalty equal to the absolute value of the coefficients, while L2 regularization adds a penalty equal to the square of the coefficients. Ridge regression is a type of linear regression that uses L2 regularization to prevent overfitting by adding a penalty term to the loss function based on the magnitude of the coefficients.



optimizer=torch.optim.AdamW(model.parameters(),lr=1e-4,weight_decay=0.01)
"""Adam - optimizer,W - weight decay (L2 regularization),lr - learning rate-0.0001"""
"""parameters- pass all weights of nn to the optimizer"""
"""optimizer updates the weights """
"""lr - controls how much the wegihts are updated""""
for epoch in range(10): #--train the model 10 times with training data"
    # Forward pass
    predictions = model(X_train)
    # Calculate loss
    loss = criterion(predictions, y_train)#loss function checks how wrong the model is.
    criterion = torch.nn.MSELoss()
    criterion = torch.nn.CrossEntropyLoss()
    # Clear old gradients
    optimizer.zero_grad()
    # Backpropagation
    loss.backward()#Which direction should each weight move to reduce the loss?Loss → Output layer → Hidden layers → Input side
    # Update weights
    optimizer.step()
    print(loss.item())