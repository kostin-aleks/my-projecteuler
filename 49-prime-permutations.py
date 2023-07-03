#!/usr/bin/env python3
"""
Prime permutations

Problem 49

The arithmetic sequence, 1487, 4817, 8147, 
in which each of the terms increases by 3330, 
is unusual in two ways: (i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms 
in this sequence?
"""
from functions import eratosthenes2, is_prime

N = 10000

primes = [x for x in eratosthenes2(N) if x > 999]
# print(primes)
# print(len(primes))

def permutation(num1, num2):
    return set(str(num1)) == set(str(num2))

# print(permutation(1487, 4817))
# print(permutation(1487, 4827))


i = 0
while i < len(primes):
    n1 = primes[i]
    j = i + 1
    while j < len(primes) - 1:
        n2 = primes[j]
        if permutation(n1, n2):
            n3 = n2 + n2 - n1
            if n3 in primes and permutation(n1, n3):
                print(f'4-digit increasing sequence {[n1, n2, n3]}')
                print(f'difference is {n2 - n1}')
                print(f'12-digit number formed by concatenating the three terms in this sequence is {n1}{n2}{n3}')
        j += 1
    i += 1



        