'''
Problem : Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
          Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
          The tests are generated such that there is exactly one solution. You may not use the same element twice.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''
"""

# 1st Solution:

numbers = list(map(int,input().split(" ")))
target = int(input())
a, b = 0, len(numbers) - 1
while a < b:
    if numbers[a] + numbers[b] == target: 
        print(a + 1,  b + 1)
    if numbers[a] + numbers[b] > target: 
        b -= 1
    else: a += 1
"""

# 2nd Solution:

numbers = list(map(int,input().split(" ")))
target = int(input())
i = 0
l = len(numbers) - 1
while i < l:
    n = numbers[i] + numbers[l]
    if n < target:
        i += 1
    if n > target:
        l -= 1
    if n == target:
        print(i+1,l+1)
        break