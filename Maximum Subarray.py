'''
Problem: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
nums = list(map(int,input().split(" ")))
ans = nums[0]
current = nums[0]
for i in nums[1:]:
    if current + i > i:
        current = current+i
    else:
        current = i
                
    if current > ans:
        ans = current
print(ans)