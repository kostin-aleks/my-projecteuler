#!/usr/bin/env python3
"""
Singular integer right triangles

Problem 75

It turns out that 12 cm is the smallest length of wire that can be bent 
to form an integer sided right angle triangle in exactly one way, 
but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer 
sided right angle triangle, and other lengths allow more than one solution to be found; 
for example, using 120 cm it is possible to form exactly three different integer 
sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, 
for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle 
be formed?
"""
import math

N = 1_500_000
# N = 100
sqrt_n = int(math.sqrt(N))

triangles = {}
for m in range(2, sqrt_n):
    for n in range(1, m):
        if (m + n) % 2 == 0:
            continue
        if math.gcd(m, n) != 1:
            continue
        
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        l = a + b + c
        # print(a, b, c, l)
        k = 1
        while k * l <= N:
            triangles[k * l] = triangles.get(k * l, 0) + 1
            k += 1
            

# print(triangles)             
cnt = 0
items = []
for k, v in triangles.items():
    if v == 1:
        items.append(k)
        cnt += 1
    
print(f'Count of such triangles is {cnt}')
# print(sorted(items))
