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