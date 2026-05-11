"""Prefix/Suffix Product Pattern"""

"""Question: Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all elements except nums[i]."""

def productofarrayexceptself(nums):
    n=len(nums)#[1,2,3,4]
    answer=[1]*n #[1,1,1,1][1,1,2,6]
    left=1
    for i in range(n):#[0,1,2,3]
        answer[i]=left
        left*=nums[i]

    right=1
    for i in range(n-1,-1,-1):
        answer[i]*=right
        right*=nums[i]

        return answer
    

    """How do you encode categorical variables in machine learning?"""
    import pandas as pd
    df=pd.dataFrame({
        "Color": ["Red","Green","Blue","Red"]})
    
    encoded_df=pd.get_dummies(df,columns=["Color"]  )
    print(encoded_df)

" Question: What is Gradient Descent in Machine Learning?"

from sklearn.linear_model import SGDRegressor
from sklearn.datasets import make_regression

X,y=make_regression(n_samples=100,n_features=1,noise=10,random_state=42)

model=SGDRegressor(max_iter=1000,learning_rate="constant",eta0=0.01)
model.fit(X, y)

print("Training complete")

        



