#!/usr/bin/env python

"""
Combine
"""

def combine(gen_a, gen_b):
    list_a: list[object] = []
    list_b: list[object] = []
    a_active = True
    b_active = True
    c = 0
    while True:
        if a_active:
            try:
                list_a.append(next(gen_a))
            except StopIteration:
                gen_a.close()
                a_active = False
        if b_active:
            try:
                list_b.append(next(gen_b))
            except StopIteration:
                gen_b.close()
                b_active = False
        start = c - len(list_b) + 1
        end = len(list_a)
        if start == end:
            break
        yield [(list_a[i], list_b[c - i]) for i in range(start, end)]
        c += 1


def main():

    def gen_a():
        yield from [1, 2, 3, 4]

    def gen_b():
        yield from [1, 2, 3, 4]

    for y in combine(gen_a(), gen_b()):
        print(y)
