#!/usr/bin/env python3
"""
Spiral primes

Problem 58

Starting with 1 and spiralling anticlockwise in the following way, 
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals 
are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, 
a square spiral with side length 9 will be formed. 
If this process is continued, what is the side length of the square spiral 
for which the ratio of primes along both diagonals first falls below 10%?
"""
from functions import is_prime, eratosthenes2, is_prime_number

# закономерности для чисел на диагонали
# a(n) = n^2 полудиагональ с квадратами, правая нижняя
# b(n) = n^2 - 3n + 3 полудиагональ правая верхняя
# c(n) = n^2 - 2*n + 2 полудиагональ левая верхняя
# d(n) = n^2 - n + 1 полудиагональ левая нижняя
# n = 3, 5, 7, ... размер матрицы

N = 100_000_000
# all_primes = list(eratosthenes2(N))

cnt = 1 # количество диагональных элементов
primes = 0
for n in range(3, 30000, 2):
    a = n * n
    if is_prime_number(a):
        primes += 1
    b = n * n - 3 * n + 3
    if is_prime_number(b):
        primes += 1
    c = n * n - 2 * n + 2
    if is_prime_number(c):
        primes += 1
    d = n * n - n + 1
    if is_prime_number(d):
        primes += 1
    cnt += 4
    ratio = primes / cnt
    print(f'size:{n:5d}, primes:{primes:5d}, count:{cnt:6d}, ratio:{ratio:1.4f}')
    if ratio < 0.1:
        print(f'matrix size is {n}, ratio is {ratio:1.10f}')
        break

