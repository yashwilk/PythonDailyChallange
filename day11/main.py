#Grouping items by a common key and storing lists as values.

students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "B"),
    ("Eve", "C")
]



grouped={}

for val,key in students:
    if key not in grouped:
        grouped[key]=[]
    grouped[key].append(val)
print(grouped)

#Iterating through characters and building new strings.
text = "hello world"

result=""

for char in text:
    if char.lower() not in "aeiou":
        result+=char

#Understanding how sorting can normalize strings for comparison.
word1="listen"
word2="silent"

sorted1=sorted(word1)
sorted2=sorted(word2)

if sorted1==sorted2:
    print("Anagrams")
else:
    print("Not anagrams")


#Using arrays or maps to count occurrences of each character.
text='banana'
freq={}

for char in text:
    if char not in freq:
        freq[char]=0
    freq[char]+=1

#Creating immutable, hashable keys from mutable data.
my_dict = {}
key = [1, 2, 3]

my_dict[tuple(key)]="value"




words = ["eat", "tea", "tan", "ate", "nat", "bat"]

group={}

for word in words:
    key=tuple(sorted(word))
    if key not in group:
        group[key]=[]
    group[key].append(word)

print(group.values())




#Using dictionaries to count element frequencies efficiently.
nums = [1, 1, 1, 2, 2, 3]

freq={}

for num in nums:
    if num not in freq:
        freq[num]=0
        
    freq[num]+=1

print(freq)


#Sorting elements by custom criteria.
nums = [1, 1, 1, 2, 2, 3]
freq={}
#Increase the count of this number by 1.If the number is not already in the dictionary, start from 0.
for num in nums:
    freq[num]=freq.get(num,0)+1

    """{1:3,
     2:2,
     3:1}"""

    sorted_nums=sorted(freq.items(),key=lambda x:x[1],reverse=True)


#Using min-heaps to maintain top k elements efficiently.

import heapq

nums = [1, 1, 1, 2, 2, 3]

freq={}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

k=2
heap=[]
for num, count in freq.items():
    heapq.heappush(heap,(-count,num))
    if len(heap) > k:
        heapq.heappop(heap)

result=[]

for _ in range(k):
    result.append(heapq.heappop(heap)[1])

    
print(result)

"""
for num, count in freq.items():
    heap.append([count,num])
heap.sort()
res=[]
while len(res)<k:
    res.append(heap.pop()[1])
            return res


"""




#Find two numbers that add to target
nums = [1, 2, 3, 4, 6]
target = 6

left=0
right=len(nums)-1

while left<right:
    currentsum=nums[left]+nums[right]
    if currentsum==target:
        print(nums[left],nums[right])
        break
    elif currentsum<target:
        left+=1
    else:
        right-=1

#Used to find a target in a sorted array
nums = [1, 3, 5, 7, 9, 11]
target = 7

left=0
right=len(nums)-1

while left<=right:
    mid=(left+right)//2
  
    if nums[mid] == target:
        print("Found at index:", mid)
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1


#Two Sum using Dictionary
nums = [2, 7, 11, 15]
target = 9

seen={}

for i,num in enumerate(nums):
    complement=target-num
    if complement in seen:
        print(seen[complement],i)
        break
    seen[num]=i


def threeSum(nums):

    res=set()
    nums.sort()

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k]==0:
                    temp=[nums[i], nums[j], nums[k]]
                    res.add(tuple(temp))

    return [list(x) for x in res]
                


nums = [-1, 0, 1, 2, -1, -4]

nums.sort()

result=[]

for i in range(len(nums)):
    if i>0 and nums[i]==nums[i-1]:
        continue
    left=i+1
    right=len(nums)-1
    while left<right:
        total=nums[i]+nums[left]+nums[right]
        if total==0:
            result.append([nums[i], nums[left], nums[right]])


            left += 1
            right -= 1
            
            while left < right and nums[left] == nums[left - 1]:
                left += 1

            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        elif total < 0:
            left += 1

        else:
            right -= 1

print(result)   