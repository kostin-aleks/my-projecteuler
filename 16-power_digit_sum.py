#!/usr/bin/env python3
"""
Power digit sum
 
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

exp = 1000

digit_sum = 0
value = 2 ** exp
print(f'2^{exp} equals {value}')
while value >= 1:
    digit = value % 10
    digit_sum += digit
    value //= 10
    
print(f'Sum of the digits is {digit_sum}')

