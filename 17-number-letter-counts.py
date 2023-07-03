#!/usr/bin/env python3
"""
Number letter counts
 
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""
from functions import int_to_en

def count_of_chars(number_str):
    """
    count of chars in string exclude spaces and hyphens
    """
    return len([x for x in number_str if x not in (' ', '-')])

number = 342 
string = int_to_en(number)
# print(number, string, count_of_chars(string))

summ = 0

for number in range(1, 1001):
    summ += count_of_chars(int_to_en(number))

print(f'{summ} letters are used for all numbers from 1 to 1000 inclusive (numbers are written out in words)')
