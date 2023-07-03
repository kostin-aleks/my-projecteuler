#!/usr/bin/env python3
"""
Smallest multiple

Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

import functools


def prime_factors(n):
    """
    раскладывает натуральное число
    на простые множители
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

    
def list_difference(lst, lst2):
    """
    возвращает список элементов из lst2
    которых нет в lst
    """
    lst1 = lst.copy()
    i = 0
    while i < len(lst2):
        k = lst2[i]
        if k in lst1:
            lst1.remove(k)
            lst2.remove(k)
            i = 0
            continue
        i += 1
        
    return lst2


factors = []

for k in range(2, 21):
    n_factors = prime_factors(k)
    factors.extend(list_difference(factors, n_factors))

print(f'factors={sorted(factors)}')
print(f'product={functools.reduce(lambda a, b: a * b, factors)}')
