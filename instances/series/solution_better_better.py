#!/usr/bin/env python

"""
Solution
"""

size=1000000
cache_dict = {}

max_value=-1
max_position=-1
for i in range(1, size):
    count = 0
    series=[]
    n = i
    while n!=1:
        if n in cache_dict:
            count = cache_dict[n]+len(series)
            break
        series.append(n)
        n = n / 2 if n % 2 == 0 else n * 3 + 1
        count +=1
    if count>max_value:
        max_position=i
        max_value=count
    for k in series:
        cache_dict[k]=count
        count-=1
print("max_position", max_position)
print("max_value", max_value)
print("size of dict is", len(cache_dict))
print("max value is", max(cache_dict.keys()))
