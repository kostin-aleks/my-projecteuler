#!/usr/bin/env python3
"""
Factorial digit sum
 
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

def factorial(n):
    """
    calculates factorial for n
    """
    result = 1
    for m in range(2, n + 1):
        result *= m
    return result

n = 100
value = factorial(100)
print(f'{n}! = {value}')

digit_sum = 0
while value >= 1:
    digit = value % 10
    digit_sum += digit
    value //= 10

print(f'The sum of the digits in the number {n}! is {digit_sum}')
