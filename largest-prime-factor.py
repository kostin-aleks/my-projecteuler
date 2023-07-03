#!/usr/bin/env python3

def prime_factors(n):
     i = 2
     factors = []
     while i * i <= n:
          if n % i:
               i += 1
          else:
               n //= i
               factors.append(i)
     if n > 1:
          factors.append(n)
     return factors

factors = prime_factors(600851475143)

print(factors[-1])

