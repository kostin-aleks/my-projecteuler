#!/usr/bin/env python3
"""
Non-abundant sums

Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
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


max_n = 28123

perfect = []
deficient = []
abundant = []

for x in range(2, max_n):
    divisors = list(divisor_generator(x))[:-1]
    # print(x)
    # print(divisors)
    total = sum(divisors)
    # print(total)
    # print('---------')
    if total == x:
        perfect.append(x)
    if total < x:
        deficient.append(x)
    if total > x:
        abundant.append(x)
        
print(len(perfect))
print(f'count of abandon is {len(abundant)}')
print(len(deficient))

print(perfect)
# print(abundant)

def sum_of_two_abundant(k, abundant):
    for m in abundant:
        for z in abundant:
            if m + z == k:
                print(f'{k} is sum of {m} and {z}')
                return True
            if m + z > k:
                break
    return False

min_abundant = min(abundant)
print(f'min abundant is {min_abundant}')

sums = []
for i in range(len(abundant)):
    print(i)
    for item in abundant[i+1:]:
        sums.append(abundant[i] + item)
        
print(len(sums))
sums = [x for x in sums if x <= max_n]
print(len(sums))
sums = set(sums)
print(len(sums))

numbers = set([x for x in range(max_n + 1)])
result = list(numbers - sums)

summ = sum(result)
#summ = 0
#for k in range(min_abundant, max_n):
    #print(k)
    #if not sum_of_two_abundant(k, abundant):
        #summ += k
        #print('added')
        
print(summ)
    