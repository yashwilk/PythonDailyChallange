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


#Sliding window Expand the window → move right pointer Shrink the window → move left pointer
#Sliding window+set
s = "abcabcbb"
char_set=set()
left=0
max_length=0
for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left+=1
    char_set.add(s[right]) 

    max_length = max(max_length, right - left + 1)




#sliding window+map
s = "abcabcbb"
char_index={
}
left=0
max_length=0

for right in range(len(s)):
    if s[right] in char_index:
        left=max(left,char_index[s[right]]+1)
    char_index[s[right]]=right
    max_length=max(max_length,right-left+1)

print(max_length)


#Longest Repeating Character Replacement
s = "AABBC"
k = 1
res=0
count={}
maxf=0
left=0
for right in range(len(s)):
    count[s[right]]=count.get(s[right],0)+1
    maxf=max(maxf,count[s[right]])
    while(right-left+1)-maxf>k:
        count[s[left]]-=1
        left+=1
    res=max(res,right-left+1)
print(res)


#stack ---like a stack of book adss one by one removes from top
stack=[]
stack.append(4)
stack.append(5)
stack.append(6)
stack.pop()
#String Parsing
token = "25"
if token.isdigit():
    number=int(token)
token = "+"
if token in ["+","-","/","*"]:
    print("operator")

#n postfix notation:operator comes AFTER operands
#23+ is 2+3
tokens = ["1","2","+","3","*","4","-"]

stack=[]

for c in tokens:
    if c=="+":
        stack.append(stack.pop()+stack.pop())
    elif c=="-":
        stack.append(stack.pop()-stack.pop())
    elif c=="*":
        stack.append(stack.pop()*stack.pop())
    elif c=="/":
        a,b=stack.pop(),stack.pop()
        stack.append(int(float(b)/a))
    else:
        stack.append(int(c))

print(stack[0])



temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
n = len(temperatures)
res = [0] * n
for i in range(n-2, -1, -1):
    j = i + 1
    while j < n and temperatures[j] <= temperatures[i]:
        if res[j] == 0:
            break
        j += res[j]
    if j < n and temperatures[j] > temperatures[i]:
        res[i] = j - i

print(res)


def CarFleet(target, position, speed):
    pair = list(zip(position, speed))
    pair.sort(reverse=True)
    stack = []
    for p, s in pair:
        time = (target - p) / s
        stack.append(time)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


