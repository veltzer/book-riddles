#!/usr/bin/env python

"""
https://en.wikipedia.org/wiki/Birthday_problem

For groups of several sizes, simulate many groups of people with random
birthdays (365 days, no leap years) and print the fraction of groups in which
two people share a birthday, next to the exact probability.
"""

import random

DAYS = 365
TRIALS = 100000


def exact(n):
    """ Probability that at least two of n people share a birthday. """
    all_different = 1.0
    for i in range(n):
        all_different *= (DAYS - i) / DAYS
    return 1 - all_different


def simulate(n):
    """ Fraction of TRIALS random groups of n people with a shared birthday. """
    shared = 0
    for _ in range(TRIALS):
        birthdays = [random.randint(0, DAYS - 1) for _ in range(n)]
        if len(set(birthdays)) < n:
            shared += 1
    return shared / TRIALS


for size in (10, 20, 23, 30, 50):
    print(f"{size} people: simulated {simulate(size):.4f}, exact {exact(size):.4f}")
