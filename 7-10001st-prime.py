#!/usr/bin/env python3
"""
10001st prime

Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""
import math

lst = []


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
N = 110000
for k in eratosthenes2(N):
    lst.append(k)

print(f'количество простых чисел в диапазоне до {N} равно {len(lst)}')
print(f'10001-е простое число равно {lst[10000]}')





