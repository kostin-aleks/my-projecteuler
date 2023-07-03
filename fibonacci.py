#!/usr/bin/env python3

a, b = 1, 2
s = 2

print(a, b)

while a < 4000000:
    a, b = b, a + b
    # print(b)
    if b < 4000000 and b % 2 == 0:
        s += b
print(s)
