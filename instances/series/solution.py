#!/usr/bin/env python

"""
Solution
"""

size=1000000

max_value=-1
max_position=-1
for i in range(1, size):
    if i%1000==0:
        print("got to", i)
    count = 0
    n = i
    while n!=1:
        n = n / 2 if n % 2 == 0 else n * 3 + 1
        count +=1
    if count>max_value:
        max_position=i
        max_value=count
print("max_position", max_position)
print("max_value", max_value)
