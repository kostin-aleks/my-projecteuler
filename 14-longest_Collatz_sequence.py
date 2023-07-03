#!/usr/bin/env python3
"""
Longest Collatz sequence

Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def collatz_sequence(start):
    seq = [start]
    while seq[-1] != 1:
        x = seq[-1]
        if x % 2 == 0:
            seq.append(x // 2)
        else:
            seq.append(3 * x + 1)
    
    return seq

# print(collatz_sequence(13))

N = 1000000
max_len = 0
max_start = None

for start in range(2, N):
    seq = collatz_sequence(start)
    # print(start, len(seq))
    seq_len = len(seq)
    if seq_len > max_len:
        max_len = seq_len
        max_start = start

print(f'Starting numbers are under {N}')        
print(f'Longest sequence is {max_len} for starting number {max_start}')

