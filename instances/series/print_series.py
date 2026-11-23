#!/usr/bin/env python

"""
Print series
"""

n=77031
while n!=1:
    print(n)
    n = n / 2 if n % 2 == 0 else n * 3 + 1
