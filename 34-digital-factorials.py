#!/usr/bin/env python3
"""
Digit factorials

Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from functions import factorial

factorials = {k:factorial(k) for k in range(10)}

lst = []
for n in range(10, 3_000_000):
    digits = [int(x) for x in str(n)]
    summ = sum([factorials[x] for x in digits])
    if summ == n:
        lst.append(n)
        # print(n)

print(f'all curious numbers which are equal to the sum of the factorial of their digits are {lst}')
print(f'The sum of numbers is {sum(lst)}')