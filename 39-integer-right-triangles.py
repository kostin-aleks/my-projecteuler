#!/usr/bin/env python3
"""
Integer right triangles
 
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import math


max_perimeter = 1000
# a <= 500
# b <= 500

perimeters = {}

for a in range(1, 501):
    for b in range(1, 501):
        c = math.sqrt(a ** 2 + b ** 2)
        if c % 1 == 0:
            p = int(a + b + c)
            if p <= max_perimeter:
                perimeters[p] = perimeters.get(p, 0) + 1
                
max_ = 0
max_p = None
for p in perimeters:
    if perimeters[p] > max_:
        max_ = perimeters[p]
        max_p = p
        
# print(perimeters)
print(f'For perimeter {max_p} number of solutions is maximised, {max_}')
