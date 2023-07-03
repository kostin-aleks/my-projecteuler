#!/usr/bin/env python3
"""
Lexicographic permutations
 
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
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

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for permutation in permutations(lst):
    counter += 1
    print(permutation, counter)
    if counter == 1_000_000:
        break

last_permutation = ''.join([str(x) for x in permutation])
print(f'The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 is {last_permutation}')
