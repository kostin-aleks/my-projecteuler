#!/usr/bin/env python3
"""
Summation of primes

Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

import math


def eratosthenes2(n):
    """
    решето Эратосфена для простых чисел
    генератор
    """
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
            
# диапазон выбран экспериментально
N = 2000000
S = sum(eratosthenes2(N))


# print(f'количество простых чисел в диапазоне до {N} равно {len(lst)}')
print(f'Сумма простых чисел  в диапазоне до {N} равно {S}')
