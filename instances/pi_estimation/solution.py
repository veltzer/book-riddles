#!/usr/bin/env python

"""
This is an example of how to estimate pi according to the statistical solution
of the PI estimation riddle

As you can see it takes quite a long time to get a to a good estimation of PI.
"""

import math  # for hypot
import random  # for uniform

samples = 1000000
good_samples = 0
print_every = 100000
for i in range(1, samples + 1):
    x = random.uniform(-0.5, 0.5)
    y = random.uniform(-0.5, 0.5)
    if math.hypot(x, y) <= 0.5:
        good_samples += 1
    if i % print_every == 0:
        print(f"after {i} samples: {4 * good_samples / i}")
print(f"estimate of pi: {4 * good_samples / samples}")
