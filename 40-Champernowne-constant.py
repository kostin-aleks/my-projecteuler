#!/usr/bin/env python3
"""
Champernowne's constant
 
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

"""

import functools


string = ''.join(str(x) for x in range(1_000_000))
print(f' Длина строки {len(string)}')

lst = [string[1], string[10], string[100], string[1000], 
      string[10000], string[100000], string[1000000]]

numbers = [int(x) for x in lst]
print(numbers)

product = functools.reduce(lambda a, b: a * b, numbers)
print(f'Произведение равно {product}')
