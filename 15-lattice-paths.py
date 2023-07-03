#!/usr/bin/env python3
"""
Lattice paths

Problem 15

Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from functools import reduce

# Quick No Programming Solution (based on combinatorics)

# I take it "no backtracking" means we always either increase x or increase y.

# If so, we know that in total we will have 40 steps to reach the finish
# -- 20 increases in x, 20 increases in y.

# The only question is which of the 40 are the 20 increases in x. 
# The problem amounts to: how many different ways can you choose 
# 20 elements out of a set of 40 elements. 
# (The elements are: step 1, step 2, etc. 
# and we're choosing, say, the ones that are increases in x).

# There's a formula for this: it's the binomial coefficient 
# with 40 on top and 20 on the bottom. 
# The formula is 40!/((20!)(40-20)!), in other words 40!/(20!)^2. 
# Here ! represents factorial. (e.g., 5! = 5*4*3*2*1)

# Canceling out one of the 20! and part of the 40!, 
# this becomes: 
# (40*39*38*37*36*35*34*33*32*31*30*29*28*27*26*25*24*23*22*21)/
# (20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1). 
# The problem is thus reduced to simple arithmatic. 
# 
# N = (w + h)! / (w! * h!) where w is width and h is height of grid.

N = reduce(lambda a, b: a * b, list(range(21, 41))) \
    / reduce(lambda a, b: a * b, list(range(1, 21)))

N = int(N)

print(f'Count of routes is {N}')



