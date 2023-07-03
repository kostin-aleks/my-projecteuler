#!/usr/bin/env python3
"""
Square root convergents

Problem 57

It is possible to show that the square root of two can be expressed 
as an infinite continued fraction.
sqrt(2) = 1 + 1 / (2 + 1 / (2 + 1 / ...)) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...



The next three expansions are 99/70, 239/169, and 577/408, 
but the eighth expansion, 1393/985, is the first example where the number 
of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, 
how many fractions contain a numerator with more digits than the denominator?
"""

# Solution
# Iteration can be described as:
# f(n + 1) = 1 + 1 / (2 + f(n))
#
# Each iteration is a fraction, let's call it f(n) = a(n) / b(n)
#
# f(n + 1) = 1 + 1 / (1 + a(n) / b(n)) = 1 + 1 / (b(n) + a(n) / b(n)) =
# = 1 + b(n) / (b(n) + a(n)) = (b(n) + a(n) + b(n)) / (b(n) + a(n))
#
# a(n + 1) / b(n + 1) = (2b(n) + a(n)) / (b(n) + a(n))
# so 
# a(n + 1) = 2b(n) + a(n)
# b(n + 1) = b(n) + a(n)

# initial values
# x(0) = 1 + 1/2 = 1 + 1 / (1 + 1)
# a(0) = 1
# b(0) = 1

cnt = 0
a = 1
b = 1
a1 = None
b1 = None

for i in range(1000):
    a1 = 2 * b + a
    b1 = b + a
    numerator = str(a1)
    denominator = str(b1)
    if len(numerator) > len(denominator):
        cnt += 1
        # print(i, len(numerator), len(denominator))
    a = a1
    b = b1

print(f'In the first one-thousand expansions are {cnt} fractions')
print(f'contain a numerator with more digits than the denominator')

