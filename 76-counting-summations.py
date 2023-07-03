#!/usr/bin/env python3
"""
Counting summations

Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written 
as a sum of at least two positive integers?
"""

target = 8

ways = [1] + [0] * target

for n in range(1, target):
    for i in range(n, target + 1):
        ways[i] += ways[i - n]
        
print(f'Number of ways {target} can be written as sum of at least two positive integers: {ways[target]}')

