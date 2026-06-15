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
import math
import pandas as pd
from typing import List

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




matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



print(matrix[0][0])

for row in matrix:
    for value in row:
        print(value,end=" ")


row=len(matrix)
col=len(matrix[0])

for r in range (row):
    for c in range(col):
        print(matrix[r][c])




#Sometimes a matrix is treated like a single 1D array.
index=4
rows=index//col
cols=index%col

print(matrix[rows][cols])


#Convert 2D Coordinates → 1D Index
index = row * cols + col

#Binary Search works only on sorted data.
arr = [2, 4, 6, 8, 10, 12, 14]
target=10

def binary_search(arr,target):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        
        if arr[mid]<target:
            left=mid+1

        else:
            right=mid-1
    return -1

search=[[1,  3,  5],
[7  ,9, 11],
[13 ,15 ,17]]


def single_binary_search(search,target):
    rows=len(search)
    cols=len(search[0])

    left=0
    right=rows*cols-1
    while left<=right:
        mid=(left+right)//2

        r=mid//cols
        c=mid%cols

        value=search[r][c]

        if value==target:
            return True
        elif value < target:
            left =mid+1
        else:
            right =mid-1

    return False


def double_binary_search(search,target):
    rows=len(search)
    col=len(search[0])

    top=0
    bottom=rows-1

    while top<=bottom:
        row=(top+bottom)//2
        if target>search[row][col-1]:
            top=row+1
        elif target<search[row][0]:
            bottom=row-1
        else:
            break
    left=0
    right=col-1
    while left<=right:
        mid=(left+right)//2
        value= search[row][mid]
        if value == target:
            return True

        elif value < target:
            left = mid + 1

        else:
            right = mid - 1

    return False  


piles = [3, 6, 7, 11]
h = 8

def minEatingSpeed(piles, h):
    left=1
    right=max(piles)

    while left<=right:
        mid=(left+right)//2
        total_hours=0
        for pile in piles:
            total_hours+=math.ceil(float(pile)/mid)
        if total_hours<=h:
            right=mid-1
        else:
            left=mid+1
    #mid=6
    return left


df = pd.DataFrame({
    "order_date": ["2023-01-01","2023-01-02","2023-01-03","2023-01-06","2023-01-07",
                   "2023-01-08","2023-01-09","2023-01-10","2023-01-13","2023-01-14"],
    "sales": [100, 200, 150, 300, 250, 180, 220, 170, 310, 260],
    "symbol": ["A","B","A","B","A","B","A","B","A","B"],
    "value":  [10, 20, 15, 25, 12, 22, 18, 28, 11, 21],
    "city":   ["NY","LA","NY","SF","LA","NY","SF","LA","NY","SF"],
    "age":    [25, 17, 35, 45, 22, 55, 30, 28, 42, 19],
    "Department": ["Sales","IT","HR","Sales","IT","HR","Sales","IT","HR","Sales"],
    "Salary": [50000,60000,45000,55000,65000,48000,52000,62000,46000,58000],
    "store":  ["S1","S2","S1","S2","S1","S2","S1","S2","S1","S2"],
})

df["order_date"] = pd.to_datetime(df["order_date"])
df["weekday"] = df["order_date"].dt.weekday
df["is_weekend"] = df["weekday"].isin([5, 6]).astype(int)
df["sales_lag_1"] = df["sales"].shift(1)
df["rolling_mean_7"] = df["sales"].rolling(7).mean()

df["rolling_std_7"] = df["sales"].rolling(7).std()
df.groupby("symbol")["value"].transform("mean")

freq = df["city"].value_counts()
df["age_group"] = pd.cut(df["age"],bins=[0,18,30,50,80],labels=["a","b","c","d"])

pd.get_dummies(df, columns=["city"])


df["salary"]=df.groupby("Department")["Salary"].transform(lambda x: x.fillna(x.mean()))
df["rank_in_store"] = df.groupby("store")["sales"]\
                        .rank(ascending=False)
                        


#Building strings and extracting substrings using indices
first = "John"
last = "Doe"
full_name =first+ " "+last
print(full_name)

text="DataScience"

print(text[0])
print(text[9])

#Slicing
print(text[0:4])
print(text[4:11])
word = "Python"
reversed_word = word[::-1]


words = ["apple", "banana", "grape"]
encode=" ".join(words)

decode=encode.split(" ")
words = ["apple#pie", "banana"]
encide="<END>".join(words)

words=["cat", "apple", "hello"]

encoded=""
for word in words:
    encoded+=str(len(word))+"#"+word
print(encoded)
     #3#cat5#apple5#hello     
     # 
     # 
strs= ["neet","code","love","you"]

def encode(strs:List[str])->str:
    res=""
    for s in strs:
        res+=str(len(s))+"#"+s
    return res

def decode(res:str)->List[str]:
    i=0
    decode=[]
    while i<len(res):
        j=i
        while res[j]!="#":
            j+=1
        length=int(res[i:j])

        word=res[j+1:j+1+length]
        decode.append(word)

        i=j+1+length
    return decode
print(decode(encode(strs)))


#product of each number except self
def productExceptSelf(nums: List[int]) -> List[int]:
    n=len(nums)
    res=[0]*n
    pref=[0]*n
    suff=[0]*n
    pref[0]=suff[n-1]=1
    for i in range (1,n):
        pref[i]=nums[i-1]*pref[i-1]
    for i in range(n-2,-1,-1):
        suff[i]=nums[i+1]*suff[i+1]

    for i in range(n):
        res[i] = pref[i] * suff[i]
    return res


#Reinforcement Learning
#is a machine learning approach where an agent learns by interacting with an environment. Instead of learning from labelled data, it learns by trying actions and receiving rewards or penalties.
#Maze, stock market, game
#The agent wants to maximize cumulative future reward:
#The agent wants to maximize cumulative future reward:
#A high γ means the agent cares about long-term reward. A low γ means it focuses more on immediate reward.
"""Agent-environment-s(current state)
                        |
                        a(action)-r(reward or penalty)-Strategy
 
                                         |-new state-V(s)-how good is this state q(s,a)
"""

def findmin(nums:List[str])->int:
    res=nums[0]
    left=0
    right=len(nums)-1
    while left<= right:
        if num[left]<=num[right]:
            return min(res,num[left])
            break
        mid=(left+right)//2
        res=min(res,num[mid])
        if num[mid]>=num[left]:
            left=mid+1
        else:
            right=mid-1
    return res


#linked list
#Value + Pointer to next node
#traversing a linkedlist
curr=head
while curr:
    print(curr.val)
    curr=curr.next

slow=head
fast=head

while fast and fast.next:
    slow=slow.next
    fast=fast.next.next

slow.val
fast.val

#Linked List Reversal
1 → 2 → 3 → 4 → NULL
4 → 3 → 2 → 1 → NULL

prev=None
curr=head

nxt=curr.next
curr.next=prev
prev=curr
curr=nxt
head=prev

#
#L1: 1 → 2 → 3

#L2: 4 → 5 → 6

tmp1=L1.next
temp2=L2.next
l1.next=L2
L2.next=tmp1
l1=temp1
L2=temp2


def mergeTwoLists():
    slow,fast=head,head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next 

    second=slow.next
    prev=slow.next=None
    while second:
        tmp=second.next
        second.next=prev
        prev=second
        second=tmp

        
    first,second=head,prev
    while second:
        tmp2=first.next
        temp2=second.next
        first.next=second
        second.next=tmp1
        first, second = tmp1, tmp2