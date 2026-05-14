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