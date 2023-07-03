#!/usr/bin/env python3
"""
Powerful digit counts
 
Problem 63

The 5-digit number, 16807=7^5, is also a fifth power. 
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

# Можно вычислить ограничения для n и k (n ^ k)
# n < 10
# k < 22

counter = 0

for i in range(1, 10):
    power = 1
    while True:
        if power == len(str(i ** power)):
            counter += 1
            print(f'{i}^{power}')
        else:
            break
        power += 1
        
print(counter)

