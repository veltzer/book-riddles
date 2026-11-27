#!/usr/bin/env python

"""
Solution
"""

def count_zeroes_right_of(s: str) -> int:
    c = 0
    p = len(s) - 1
    while s[p] == "0":
        c += 1
        p -= 1
    return c


num = 1

for x in range(1, 101):
    num *= x
strnum = str(num)
zero_num = count_zeroes_right_of(strnum)
print(num)
print(zero_num)
