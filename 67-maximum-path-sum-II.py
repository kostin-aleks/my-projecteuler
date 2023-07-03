#!/usr/bin/env python3
"""
Maximum path sum II
 
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt 
(right click and 'Save Link/Target As...'), 
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. 
It is not possible to try every route to solve this problem, 
as there are 299 altogether! 
If you could check one trillion (1012) routes every second 
it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)
"""

with open('p067_triangle.txt') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = [int(x) for x in data[i].strip().split()]

def search(t):
    i = len(t) - 2
    while i >= 0:      
        j = 0
        while j <= i:
            t[i][j] += max(t[i + 1][j], t[i + 1][j + 1])
            j += 1
        i -= 1
    return t[0][0]

result = search(data)

print(f'the maximum total from top to bottom of the triangle is {result}')
