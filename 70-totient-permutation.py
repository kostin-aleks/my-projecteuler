#!/usr/bin/env python3
"""
Totient permutation
 
Problem 70

Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than 
or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, 
are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n 
and the ratio n/φ(n) produces a minimum.
"""
from functions import eratosthenes2
import math
from itertools import *

# print(math.gcd(3, 6))
# print(math.gcd(3, 7))

def phi(n):
    primes = [x for x in range(1, n) if math.gcd(x, n) == 1]
    return 1 if n == 1 else len(primes)

# test
#print(phi(9))
#print(phi(1))
#print(phi(2))
#print(phi(87109))
#print(phi(100))

#def is_permutation(m, n):
    #return set(str(m)) == set(str(n))

# test
#print(is_permutation(89532, 52983))
#print(is_permutation(89539, 52983))

# это очень долго, тупик
#min_ = 1e6
#min_n = None
#for n in range(2, 10000000):
    #ph = phi(n)
    #if is_permutation(ph, n):
        #ratio = n / ph
        #print(n, ph, ratio)
        #if min_ > ratio:
            #min_ = ratio
            #min_n = n
#print(f'{min_n} produces minimal ratio {min_}')

"""
Solution

    n/φ(n) producing a minimum is the same as maximizing φ(n)/n, which occurs when n has as few prime factors as possible.
    φ(n) = n – 1 where n is prime, since all numbers below it are coprime by definition
    φ(n) = φ(pq) = (p − 1)(q − 1) where n is semiprime and p and q are its factors and p ≠ q.
    φ(n) = φ(p2) = (p − 1)p where n is semiprime and p is its only distinct factor.
    n – 1 cannot be a permutation of n, so our n cannot be a prime, but it is likely the product of two primes (semiprime).

So I just calculate all semiprimes within [2, 10000000) and very efficiently determine their totients.

Then filtering down based on whether the number and its totient are permutations is a relatively simple process.
"""

MAX = 1E7
N = 10000 * 2 # sqrt(10**7 * 2)
primes = list(eratosthenes2(N))

print(len(primes))

pairs = combinations(primes, 2)
minimum = (100, 0)
for n, t in ((a * b, (a - 1) * (b - 1)) for a, b in pairs if a * b < MAX):
    ratio = float(n) / t
    if ratio < minimum[0] and sorted(str(n)) == sorted(str(t)):
        minimum = (ratio, n)
        
print(minimum)

