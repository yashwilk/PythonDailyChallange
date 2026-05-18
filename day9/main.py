"""Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray whose sum is greater than or equal to target."""

"""Input:
target = 7
nums = [2,3,1,2,4,3]

Output:
2"""


def minSubArrayLen(target,nums):
    left=0
    current_sum=0
    min_length=float('inf')
    for right in range(len(nums)):
        current_sum+=nums[right]
        while current_sum>=target:
            min_length=min(min_length,right-left+1)
            current_sum-=nums[left]
            left+=1
    return 0 if min_length == float('inf') else min_length



"""Find the Length of the Longest Palindromic Substring

Given a string s, return the longest palindromic substring."""


"""Input:
s = "babad"

Output:
"bab"""

def longestPalindrome(s):
    result=""
    def expand(left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
            return s[left+1:right]
        for i in range(len(s)):
            odd_palindrome=expand(i,i)
            even_palindrome=expand(i,i+1)
            longest_palindrome=max(odd_palindrome,even_palindrome,key=len)
            if len(longest_palindrome)>len(result):
                result=longest_palindrome
    return result