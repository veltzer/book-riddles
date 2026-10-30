#!/usr/bin/env python

"""
Solution better

Like solution.py, but remembers the length of the series of every number below
size it has already seen: once a series reaches a remembered number, the rest of
its length is known without following it to 1. The series also climbs far above
size (into the billions), so only numbers below size are remembered.
"""

size = 1000000
# lengths[n] is the number of steps from n to 1; 0 means not known yet (and 1
# really has 0 steps)
lengths = [0] * size

max_value = -1
max_position = -1
for i in range(1, size):
    if i % 100000 == 0:
        print("got to", i)
    series = []
    n = i
    while n >= size or (n != 1 and lengths[n] == 0):
        series.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    count = lengths[n] + len(series)
    steps = count
    for k in series:
        if k < size:
            lengths[k] = steps
        steps -= 1
    if count > max_value:
        max_position = i
        max_value = count
print("max_position", max_position)
print("max_value", max_value)
