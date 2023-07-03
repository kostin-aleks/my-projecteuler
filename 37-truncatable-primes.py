#!/usr/bin/env python3
"""
Truncatable primes
 
Problem 37

The number 3797 has an interesting property. 
Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

# HackerRank gave indirectly away that all such numbers are less than 1000000

from functions import is_prime, eratosthenes2

def is_truncatable_prime(n):
    string = str(n)
    while string:
        number = int(string)
        if not is_prime(number):
            return False
        string = string[:-1]
    
    string = str(n)
    while string:
        number = int(string)
        if not is_prime(number):
            return False
        string = string[1:]
    return True


N = 1_000_000

result = []

i = 1
for k in eratosthenes2(N):
    lst = []
    if k > 10 and is_truncatable_prime(k):
        result.append(k)
        print(k)
    i += 1
    
print(f'Eleven primes that are both truncatable from left to right and right to left are {result}')
print(f'The sum of these primes are {sum(result)}')
