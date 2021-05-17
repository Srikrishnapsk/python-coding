'''
Problem: Given an integer numRows, return the first numRows of Pascal's triangle.
         In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''
num = int(input())
if num == 0:
    print([])
elif num == 1:
    print([[1]])
else:    
    a = [[1]]
    for i in range(1,num):
        r = [1]
        for j in range(1,i):
            r.append(a[i-1][j-1] + a[i-1][j])
        r.append(1)
        a.append(r)
    print(a)