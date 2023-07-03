#!/usr/bin/env python3
"""
Goldbach's other conjecture
 
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from functions import is_prime, eratosthenes2

n = 7
while True:
    n += 2
    if is_prime(n):
        continue
    prime_exists = False
    for x in range(1, n):
        square = 2 * x * x
        if square > n:
            break
        number = n - square
        if is_prime(number):
            prime_exists = True
    if not prime_exists:
        print(f'the smallest odd composite that cannot be written as the sum of a prime and twice a square is {n}')
        break



    

