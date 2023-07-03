#!/usr/bin/env python3
"""
Number spiral diagonals
 
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

N = 1001

summ = 1
i = 1
number= 1
d = 2
while i < N:
    number += d
    summ += number
    d += 2
    i += 1

# print(summ)

i = 1
d = 4
number = 1
while i < N:
    number += d
    summ += number
    i += 1
    if i % 2:
        d += 4

print(f'The sum of the numbers on the diagonals in a 1001 by 1001 spiral is {summ}')


