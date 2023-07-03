#!/usr/bin/env python3
"""
Circular primes

Problem 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from functions import is_prime, eratosthenes2


def all_primes(lst):
    """
    
    """
    numbers = [int(x) for x in lst]
    for x in numbers:
        if not is_prime(x):
            return False
    return True

        
def is_circular_prime(k):
    """
    The number, 197, is called a circular prime 
    because all rotations of the digits: 197, 971, and 719, are themselves prime.
    """
    lst = permutations(str(k))
    return all_primes(lst)

    
# функция для генерации всех циклических перестановок строки
def permutations(ch):
    lst = []
    for _ in range(len(ch) - 1):
        ch = ch[1:] + ch[0]
        lst.append(ch)
    return lst

N = 1_000_000

result = []

i = 1
for k in eratosthenes2(N):
    lst = []
    if is_circular_prime(k):
        result.append(k)
        print(k)
    i += 1

print(f'количество простых чисел в диапазоне до {N} равно {i}')
print(f'all circular primes are {result}')
print(f'количество circular primes в диапазоне до {N} равно {len(result)}')

#s = '123'
#permutations(list(s))
#for x in lst:
    #print(x)



