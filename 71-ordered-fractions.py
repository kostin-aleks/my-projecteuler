#!/usr/bin/env python3
"""
Ordered fractions

Problem 71

Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, 
we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, 
find the numerator of the fraction immediately to the left of 3/7.
"""
import math


def is_reduced_proper(n, d):
    return math.gcd(n, d) == 1


N = 1_000_000
# нереально медленно
#fractions = []
#for n in range(1, N):
    #for d in range(n + 1, N + 1):
        #if is_reduced_proper(n, d):
            #fractions.append((n, d))
            
#print(len(fractions))

a = 0
b = 1
c = 1
d = 1

while True:
    p = a + c
    q = b + d
    # print(p, q)
    if q > N:
        break
    # p / q < 3 / 7 ?
    if 7 * p < 3 * q:
        a, b = p, q
    else:
        c, d = p, q

print(f'Fraction {a}/{b} is one immediately to the left of 3/7')

    

    