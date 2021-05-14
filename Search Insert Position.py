'''
Problem: Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Input: nums = [1,3,5,6], target = 5
Output: 2
'''
nums = list(map(int,input().split(" ")))
target = int(input())
if target in nums: 
    print(nums.index(target))
else:
    nums.append(target)
    print(sorted(nums).index(target))