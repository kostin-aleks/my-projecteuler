#!/usr/bin/env python3
"""
Totient maximum
 
Problem 69

Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, 
are all less than nine and relatively prime to nine, φ(9)=6.

n 	Relatively Prime 	φ(n) 	n/φ(n)
2 	1 	                 1 	2
3 	1,2 	                 2 	1.5
4 	1,3 	                 2 	2
5 	1,2,3,4 	         4 	1.25
6 	1,5 	                 2      3
7 	1,2,3,4,5,6 	         6 	1.1666...
8 	1,3,5,7 	         4 	2
9 	1,2,4,5,7,8 	         6 	1.5
10 	1,3,7,9 	         4 	2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""
import math
from functions import eratosthenes2

# Solution
# It can be seen that the more distinct primes a number has, 
# the smaller the totient function will become. 
# Since we want to minimize φ(n)φ(n) and maximize nn to maximize
# product of (p / (p - 1))
# all we have to do is creating a number n by building the product of all primes 
# until we reach the limit.

def phi(n):
    primes = [x for x in range(1, n) if math.gcd(x, n) == 1]
    return 1 if n == 1 else len(primes)

N = 100
primes = list(eratosthenes2(N))

MAX = 1_000_000
n = 1
k = 0
while primes[k] * n <= MAX:
    n *= primes[k]
    k += 1

print(f'n={n}')

print(f'maximum of ratio is {float(n) / phi(n)}')

