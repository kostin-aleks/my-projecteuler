#!/usr/bin/env python3
"""
Sub-string divisibility
 
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number 
because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. 
In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def next_permutation(a):
    """
    get the next permutation for list a
    """
    def swap(i, j):
        a[i], a[j] = a[j], a[i]

    def reverse_tail(i):
        j = len(a) - 1
        while i < j:
            swap(i, j)
            i += 1
            j -= 1

    if len(a) <= 1:
        return False

    i = len(a) - 1
    
    while True:
        i1 = i
        i -= 1
        if a[i] < a[i1]:
            i2 = len(a)
            while True:
                i2 -= 1
                if a[i] < a[i2]:
                    break
            swap(i, i2)
            reverse_tail(i1)
            return True
        if i == 0:
            reverse_tail(0)
            return False
            
        
def permutations(a):
    """
    A generator to get permutations for list a
    """
    a = sorted(list(a))
    yield a
    while next_permutation(a):
        yield a

def is_divisible_number(lst):
    """
    группы по три цифры (слева направо) делятся на первые простые числа ?
    """
    for k in range(7):
        start = k + 1
        number = lst[start] * 100 + lst[start + 1] * 10 + lst[start + 2]
        if number % primes[k] != 0:
            return False
    return True

def lst2number(lst):
    return int(''.join(str(x) for x in lst))

primes = [2, 3, 5, 7, 11, 13, 17]
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
result = []
for permutation in permutations(lst):
    counter += 1
    # print(permutation, counter)
    if is_divisible_number(permutation):
        print(counter, permutation)
        result.append(lst2number(permutation))


print(f'all 0 to 9 pandigital numbers with this property are {result}')
print(f'sum of numbers is {sum(result)}')
