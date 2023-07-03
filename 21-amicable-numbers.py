#!/usr/bin/env python3
"""
Amicable numbers
 
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import math

def divisor_generator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)

N = 10000
amicable = []
for first in range(2, N):
    divisors = list(divisor_generator(first))[:-1]
    second = sum(divisors)
    divisors = list(divisor_generator(second))[:-1]
    summ = sum(divisors)
    if summ == first and first != second:
        print(f'amicable pair {first} and {second}')
        amicable.extend([first, second])
        
amicable = list(set(amicable))
print(f'Amicable numbers under {N} are {amicable}')

print(f'The sum of all amicable numbers is {sum(amicable)}')
