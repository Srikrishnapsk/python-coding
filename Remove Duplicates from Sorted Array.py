'''
Problem: Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
         Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
'''
nums = list(map(int,input().split(" ")))
i = 0
while i < (len(nums)-1):
    if nums[i] == nums[i+1]:
        nums.remove(nums[i])
    else:
        i=i+1
print(len(nums))