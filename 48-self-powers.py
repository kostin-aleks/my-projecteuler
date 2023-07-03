#!/usr/bin/env python3
"""
Self powers

Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

lst = [x ** x for x in range(1, 1001)]
# print(lst)

summ = sum(lst)
print(f'Sum is {summ}')
print(f'Last ten digits are {str(summ)[-10:]}')
