"""Given an integer array nums and an integer k, return the k most frequent elements.
Input:
nums = [1,1,1,2,2,3]
k = 2

Output:
[1,2]
"""
from collections import Counter
import heapq

def topkfrequent(nums,k):
    freq=Counter(nums)
    return heapq.nlargest(k,freq.keys(),key=freq.get)