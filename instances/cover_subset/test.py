#!/usr/bin/env python

"""
Test
"""

import random

import numpy as np

large_set_size = 3000
small_set_size = 10
factor_to_cover = 0.9
attempts = 1000

results = []
for _ in range(attempts):
    over = False
    small_set = set()
    large_set = set()
    iters = 0
    while not over:
        n = random.randrange(large_set_size)
        large_set.add(n)
        if n < small_set_size:
            small_set.add(n)
            if len(small_set) >= small_set_size * factor_to_cover:
                over = True
        iters += 1
    print(len(large_set))
    results.append(len(large_set) / large_set_size)
print(np.mean(results))
