"""Prefix Sum + Frequency Map” pattern"""
"""Given an array of integers nums and an integer k:

Return the total number of continuous subarrays whose sum equals k."""
"""nums = [1,1,1]
k = 2
2
nums = [1,2,3]
k = 3
2"""
"""“How many small pieces of the list add up to 3?”"""
from numpy import equal


from matplotlib.pylab import equal


def subarraysum(nums,k):
    prefix_sum=0
    count=0
    prefix_map={0:1}
    for num in nums:
        prefix_sum+=num
        if prefix_sum-k in prefix_map:
            count+=prefix_map[prefix_sum-k]
        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1
    return count

"""find the biggest sub array whose sum is equal to k"""
def max_subarray_len(nums,k):
    prefix_sum=0
    max_length=0
    prefix_map={0:-1}
    for i,num in enumerate(nums):
        prefix_sum+=num
        if prefix_sum-k in prefix_map:
            max_length=max(max_length,i-prefix_map[prefix_sum-k])
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum]=i
    return max_length







class RunningAverage:
    def __init__(self):
        self.sum = 0
        self.count = 0

    def next(self, price):
        self.sum += price
        self.count += 1

        return self.sum / self.count


avg = RunningAverage()

print(avg.next(100))
print(avg.next(200))
print(avg.next(300))