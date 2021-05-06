'''
Problem: Write a function to find the longest common prefix string amongst an array of strings.
         If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''
strs = list(map(str,input().split(" ")))
a = min(strs)
b = max(strs)
for i in range(len(a)):
    if b[i] != a[i]:
        print(b[:i])
        break