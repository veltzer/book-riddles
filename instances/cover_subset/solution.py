#!/usr/bin/env python

"""
Solution
"""

import random

import numpy

large_set_size = 1000
small_set_size = 20

print_diff = 100

stat_num = 1000

stats = [[], [], []]
for _ in range(stat_num):
    lset = set()
    sset = set()
    stop = False
    i = 0
    large_set_count = None
    small_set_count = None
    large_set_size_when_small_set_complete = None
    while not stop:
        # if i % print_diff == 0:
        #    print(len(lset), len(sset))
        r = random.randrange(large_set_size)
        if r < small_set_size:
            sset.add(r)
        lset.add(r)
        if len(sset) == small_set_size and small_set_count is None:
            small_set_count = i
            large_set_size_when_small_set_complete = len(lset)
        if len(lset) == large_set_size:
            large_set_count = i
            stop = True
        i += 1
    # the small set is a part of the large one, so it completes first
    assert large_set_size_when_small_set_complete is not None
    assert small_set_count is not None
    assert large_set_count is not None
    stats[0].append(large_set_size_when_small_set_complete)
    stats[1].append(large_set_count)
    stats[2].append(small_set_count)

print(numpy.average(stats[0]))
print(numpy.average(stats[1]))
print(numpy.average(stats[2]))
