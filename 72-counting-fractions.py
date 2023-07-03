#!/usr/bin/env python3
"""
Counting fractions

Problem 72

Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, 
we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions 
for d ≤ 1,000,000?
"""
import math


def is_reduced_proper(n, d):
    return math.gcd(n, d) == 1

def phi(n):
    primes = [x for x in range(1, n) if math.gcd(x, n) == 1]
    return 1 if n == 1 else len(primes)


N = 1_000_000
# нереально медленно
cnt = 0
#for n in range(1, N):
    #for d in range(n + 1, N + 1):
        #if is_reduced_proper(n, d):
            #cnt += 1
            #print(cnt, n, d)

# нереально медленно            
#for d in range(2, N + 1):
    #cnt += phi(d)
    #print(d, cnt)
#print(cnt)

# print(f'Fraction {a}/{b} is one immediately to the left of 3/7')

    

    