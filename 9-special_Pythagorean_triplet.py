#!/usr/bin/env python3
"""
Special Pythagorean triplet

Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

N = 1000

for a in range(1, N):
    for b in range(a + 1, N):
        c = N - (a + b)
        if c < b:
            continue
        if a**2 + b**2 == c**2:
            print(f'Pythagorean triplet is {a}^2 + {b}^2 = {c}^2')
            print(f'product = {a * b * c}')
            break

print('end')
