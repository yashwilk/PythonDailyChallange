"""two pointers"""
"""You are given an integer array height where each element represents the height of a vertical line.

Find two lines that together with the x-axis form a container that holds the most water."""

def maxarea(height):
    left=0
    right=len(height)-1
    max_area=0
    while left<right:
        width=right-left
        current_area=min(height[right],height[left])*width
        max_area=max(max_area,current_area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_area


def numislands(grid):
    if not grid:
        return 0
    rows=len(grid)
    cols=len(grid[0])
    island_count=0
    def dfs(r,c):
        if r<0 or c<0 or r>=rows or c>=cols:
            return
        if grid[r][c]=="0":
            return
        grid[r][c]="0"
        
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)      
        dfs(r,c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1":
                island_count+=1
                dfs(r,c)