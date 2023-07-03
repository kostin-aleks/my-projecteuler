#!/usr/bin/env python3
"""
Pandigital prime
 
Problem 41

We shall say that an n-digit number is pandigital 
if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
# The largest pandigital number is 987654321.
from functions import is_prime, eratosthenes2

N = 7654321

def pandigital(k):
    digits = list(str(k))
    s = set([x for x in range(1, len(digits) + 1)])
    return s == set([int(x) for x in digits])

#k = 1234
#print(k, pandigital(k))
#k = 2314
#print(k, pandigital(k))
#k = 235
#print(k, pandigital(k))

max_ = 0
for k in eratosthenes2(N):
    if pandigital(k):
        # print(k)
        if max_ < k:
            max_ = k

print(f'the largest n-digit pandigital prime is {max_}')

