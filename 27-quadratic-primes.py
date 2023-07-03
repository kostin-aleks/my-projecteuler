#!/usr/bin/env python3
"""
Quadratic primes
 
Problem 27

Euler discovered the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. 
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values 0 <= n <= 79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

def is_prime(number):
    """
    number is prime ?
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_primes(a, b):
    """
    get list of prime numbers for the formula
    n ^ 2 + a * n + b
    """
    primes = []
    n = 0
    while True:
        number = n * n + a * n + b
        if is_prime(number):
            primes.append(number)
            n += 1
        else:
            return primes
    return primes

#print(23, is_prime(23))
#print(27, is_prime(27))
#print(47, is_prime(47))

#a = -79
#b = 1601
#primes = get_primes(a, b)
#print(primes)
#print(len(primes))

max_ = 0
max_a = None
max_b = None

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        primes = get_primes(a, b)
        count = len(primes)
        if count:
            # print(count, primes)
            if max_ < count:
                max_ = count
                max_a = a
                max_b = b

print(f'{max_a} and {max_b} are coefficients for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.')
print(f'number of primes is {max_}, product of the coefficients is {max_a * max_b}')
