heapq is a Python module used to efficiently manage data in priority order where the smallest element is always quickly accessible.

import heapq
nums = [10, 5, 20, 1, 15]
heapq.heapify(nums)
heapq.heappush(nums, 3)
smallest = heapq.heappop(nums)
result = heapq.heappushpop(nums, 2)
largest = heapq.nlargest(2, nums)
smallest_two = heapq.nsmallest(2, nums)

Heapified: [1, 5, 20, 10, 15]
After heappush: [1, 5, 3, 10, 15, 20]
Popped smallest: 1
Pushpop result: 2
Heap after pushpop: [3, 5, 20, 10, 15]
2 Largest: [20, 15]
2 Smallest: [3, 5]


Counter([1,1,1,2,2,3])
{
  1: 3,
  2: 2,
  3: 1
}"""
