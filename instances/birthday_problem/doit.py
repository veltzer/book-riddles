#!/usr/bin/env python

"""
Expected number of flips of a fair coin until the first 1.

The number of flips has a geometric distribution with p=1/2, so the average
printed should be close to 1/p = 2.
"""

import random

trials = 1000000
stat = 0
for _ in range(trials):
    count = 1
    while random.randint(0, 1) != 1:
        count += 1
    stat += count
print(f"average is {stat/trials}")
