def dailytemp(temperature):
    result=[0]*len(temperature)
    stack=[]
    for i,temp in enumerate(temperature):
        while stack and temp>temperature[stack[-1]]:
            prev_index=stack.pop()
            result[prev_index]=i-prev_index
        stack.append(i)
    return result

# Merge
merged_df = pd.merge(
    df1,
    df2,
    on="ID",
    how="inner"
)



#Small est positive number that is missing
#[3, 4, -1, 1]
#missing 2


def firstmissingpositve(nums):
    n=len(nums)
    for i in range(n):
        while (1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]):
            correct_index=nums[i]-1
            nums[i],nums[correct_index]=(nums[correct_index],nums[i])
    for i in range(n):
                if nums[i]!=i+1:
                    return i+1
    return n+1


"""
[
 [1,2,2],
 [3,2,3],
 [2,4,5]
]

"""
def pacificatlantic(heights):
    rows,cols=len(heights),len(heights[0])
    pacific=set()
    atlantic=set()
    def dfs(r,c,visited,prev_height):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if (r, c) in visited:
            return
        if heights[r][c] < prev_height:
            return
        
        visited.add((r,c))

        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
             dfs(0,c,pacific,heights[0][c])
             dfs(rows-1,atlantic,heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])


        result=[]

        for cell in pacific:
             if cell in atlantic:
                result.append(list(cell))
    return result
    

