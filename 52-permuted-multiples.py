#!/usr/bin/env python3
"""
Permuted multiples
 
Problem 52

It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

N = 1_000_000
for n in range(1, N):
    digits = set(str(n))
    if digits == set(str(2 * n)):
        if digits == set(str(3 * n)):
            if digits == set(str(4 * n)):
                if digits == set(str(5 * n)):
                    if digits == set(str(6 * n)):
                        # print(n, 2 * n, 3 * n, 4 * n, 5 * n, 6 * n)
                        break

print(f'The smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits')
print(f'this number is {n}')
print(f'These permuted multiples are {n}, {2 * n}, {3 * n}, {4 * n}, {5 * n}, {6 * n}')
