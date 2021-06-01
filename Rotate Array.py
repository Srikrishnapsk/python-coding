'''
Problem: Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

# 1st Solution

nums = list(map(int,input().split(" ")))
k = int(input())
"""
Do not return anything, modify nums in-place instead.
"""
nums[:] = nums[-k%len(nums):]+nums[:-k%len(nums)]
print(nums[:])


# 2nd Solution:

nums = list(map(int,input().split(" ")))
k = int(input())
"""
Do not return anything, modify nums in-place instead.
"""
k = k%len(nums)
nums[:] = nums[-k:]+nums[:-k]
print(nums[:])
