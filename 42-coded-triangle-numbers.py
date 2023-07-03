#!/usr/bin/env python3
"""
Coded triangle numbers
 
Problem 42

The n-th term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding 
to its alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number 
then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), 
a 16K text file containing nearly two-thousand common English words, 
how many are triangle words?
"""
import math


def char_value(ch):
    return ord(ch) - ord('A') + 1

def word_value(word):
    return sum([char_value(ch) for ch in word])

def is_triangle(number):
    n = math.sqrt(2 * number + 0.25) - 0.5
    return n.is_integer()


with open('p042_words.txt') as f:
    contents = f.read()
    words = [w.strip('"') for w in contents.split(',')]
    # print(words)

print(f'count of words is {len(words)}')

result = []

for word in words:
    number = word_value(word)
    if is_triangle(number):
        # print(number, word)
        result.append(word)

print(f'All triangle words are {result}')
print(f'Count of words is {len(result)}')
