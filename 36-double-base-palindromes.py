#!/usr/bin/env python3
"""
Double-base palindromes
 
Problem 36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindrome(string):
    return string == string[::-1]

result = []
for n in range(1_000_000):
    if is_palindrome(str(n)):
        if is_palindrome(bin(n)[2:]):
            result.append(n)

print(f'Double-base palindromes , less than one million, {result}')
print(f'The sum of all numbers is {sum(result)}')
