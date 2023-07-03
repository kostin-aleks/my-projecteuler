#!/usr/bin/env python3
"""
Names scores
 
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def char_score(char):
    return ord(char) - ord('A') + 1


def alphabetical_value(name):
    total = 0
    for ch in name:
        total += char_score(ch)
    return total

    
with open('p022_names.txt') as f:
    txt = f.read()

names = [x.strip('"') for x in txt.split(',')]
names.sort()

print(f'Count of names {len(names)}')

total = 0
i = 0
while i < len(names):
    total += (i + 1) * alphabetical_value(names[i])
    i += 1
    
print(f'Total of all the name scores equals {total}')



    
