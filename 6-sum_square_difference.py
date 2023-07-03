#!/usr/bin/env python3
"""
Sum square difference

Problem 6

The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

N = 100

lst = list(range(1, N + 1))

sum_square = sum(list(map(lambda x: x * x, lst)))

square_sum = pow(sum(lst), 2)

print(f'sum of the squares {sum_square}')
print(f'square of the sum {square_sum}')

print(f'Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum equal {square_sum - sum_square}.')