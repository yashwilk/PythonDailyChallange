"""Sliding Window Pattern"""
"""Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring."""

def Lengthoflongestsubstring(s):
    seen={}
    left=0
    max_length=0
    for right in range(len(s)):
        if s[right] in seen and seen[s[right]]>=left:
            left=seen[s[right]]+1
        seen[s[right]]=right
        max_length=max(max_length,right-left+1)
    return max_length


"""Question: How do you handle missing values in a Pandas DataFrame?"""
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Age": [25, np.nan, 30, 22],
    "Salary": [50000, 60000, np.nan, 45000]
})
print(df.isnull().sum())

df['Age']=df['Age'].fillna(df['Age'].mean())
df["Salary"]=df["Salary"].fillna(df["Salary"].mean() )
print(df)


"""What is Overfitting in Machine Learning and how do you prevent it?"""
"""Overfitting happens when a model learns training data too well, including noise and unnecessary patterns, causing poor performance on unseen data."""
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


data=load_iris()
X=data.data
y=data.target


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=DecisionTreeClassifier(max_depth=3)
model.fit(X_train,y_train)

trian_accuracy=accuracy_score(y_train,model.predict(X_train))
test_accuracy=accuracy_score(y_test,model.predict(X_test))
print(f"Training Accuracy: {trian_accuracy}")   
print(f"Test Accuracy: {test_accuracy}")   



