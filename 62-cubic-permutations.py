#!/usr/bin/env python3
"""
Cubic permutations
 
Problem 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits 
which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
     
cubes = {}
cubes_lists = {}
for n in range(100, 10000):
    cube = n ** 3
    lst = sorted(str(cube), reverse=True)
    string = ''.join([str(x) for x in lst])
    cubes[string] = (cubes.get(string) or 0) + 1
    cubes_lists[string] = cubes_lists.get(string) or []
    cubes_lists[string].append(cube)
    
# print(len(cubes.keys()))
items = sorted(cubes.items(), key=lambda x: x[1], reverse=True)

# print(items[:20])
numbers = []
for item in items:
    if item[1] < 5:
        break
    s = item[0]
    print(s)
    print(cubes_lists.get(s))
    numbers.append(min(cubes_lists.get(s)))
    
print(f'{min(numbers)} is the smallest cube for which exactly five permutations of its digits are cube')







    