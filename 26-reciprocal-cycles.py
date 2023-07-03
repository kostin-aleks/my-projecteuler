#!/usr/bin/env python3
"""
Reciprocal cycles
 
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from decimal import Decimal


def recurring_cycle(n, d):
    # solve 10^s % d == 10^(s+t) % d
    # where t is length and s is start
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0

# 1
for d in range(1, 1000):
    x = Decimal(1.0) / Decimal(d)
    # print(f'{x:.30f}')
    fractional_part = str(x)[2:]
    cycle = recurring_cycle(1, d)
    # print(f'{d:5d} {fractional_part:30s} {cycle:10d}')

# 2    
num = longest = 1
for n in range(3, 1000, 2):
    if n % 5 == 0:
        continue

    p = 1
    while (10 ** p) % n != 1:
        p += 1

    if p > longest:
        num, longest = n, p

print(f'''The value of d < 1000 for which 1/d contains the longest recurring cycle 
          in its decimal fraction part is {num}, cycle is {longest}''')

