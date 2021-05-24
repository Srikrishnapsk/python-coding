'''
Problem: Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
         The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
'''
nums1 = list(map(int,input().split(" ")))
m = int(input()) 
nums2 = list(map(int,input().split(" "))) 
n = int(input())
while m > 0 and n > 0:
    if nums1[m - 1] > nums2[n - 1]:
        nums1[m + n - 1] = nums1[m - 1]
        m -= 1
    else:
        nums1[m + n - 1] = nums2[n - 1]
        n -= 1    
print(nums1[:])