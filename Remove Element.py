'''
Problem: Given an array nums and a value val, remove all instances of that value in-place and return the new length.
         Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
         The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
             It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.
'''

nums =list(map(int,input().split(" ")))
val = int(input())
while val in nums:
    nums.remove(val)
print(nums)
print(len(nums))