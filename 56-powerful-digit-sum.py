#!/usr/bin/env python3
"""
Powerful digit sum

Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, 
what is the maximum digital sum?
"""

max_ = 0
max_a = None
max_b = None
max_number = None

sums = []
for a in range(1, 100):
    for b in range(1, 100):
        number = a ** b
        string = str(number)
        summ = sum([int(x) for x in string])
        sums.append(summ)
        if summ > max_:
            max_ = summ
            max_a = a
            max_b = b
            max_number = string

print(f'{max_a}^{max_b} has maximum digital sum {max_}')
print(f'It is number {max_number}')
print(f'Length of number is {len(max_number)}')

# one string solution
print(max(sum(map(int, str(a**b))) for a in range(100) for b in range(100)))
# print(sorted(sums[-5:]))


        