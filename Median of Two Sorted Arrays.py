'''
Problem: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
nums1 = list(map(int,input().split(" ")))
nums2 = list(map(int,input().split(" ")))
nums1.extend(nums2)
nums1.sort()
n = len(nums1)
if n%2 == 0:
    print((nums1[int(n/2)]+nums1[int((n-1)/2)])/2)
else:
    print([int(n/2)])