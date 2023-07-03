#!/usr/bin/env python3
"""
Consecutive prime sum
 
Problem 50

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes 
that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand 
that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, 
can be written as the sum of the most consecutive primes?
"""
from functions import eratosthenes2, is_prime

MAX = 1_000_000

primes = [x for x in eratosthenes2(MAX)]

print(primes[-5:])
print(len(primes))

N = len(primes)
max_sum = 0
max_lst = []
max_length = 0
i = 0
while i < N - 1:
    # print(i)
    summ = primes[i]
    j = i + 1
    lst = [primes[i]]
    while j < N:
        summ += primes[j]
        lst.append(primes[j])
        #print('===', summ, lst)
        if summ in primes:
            if max_length < len(lst):
                max_length = len(lst)
                max_sum = summ
                max_lst = lst[:]
                # print(summ, lst)
        if summ > MAX:
            break
        j += 1
    i += 1

print(f'Prime number {max_sum} can be written as the sum of the most consecutive primes')
print(f'Count of consecutive primes is {max_length}')
print(f'Consecutive primes are {max_lst}')

