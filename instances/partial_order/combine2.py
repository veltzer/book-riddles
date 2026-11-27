#!/usr/bin/env python

"""
Combine 2
"""

def gen(*data):
    yield from data


def append_next_or_drop(a, aa, bb):
    try:
        aa.append(next(a))  # either append one new item to aa...
    except StopIteration:
        a.close()  # This may be called more than once --- but this is ok.
        bb.pop(0)  # or pop of the first element of bb.


def combine(a, b):
    aa: list[object] = []
    bb: list[object] = []
    while True:
        append_next_or_drop(a, aa, bb)
        append_next_or_drop(b, bb, aa)
        if len(aa) == 0:
            break
        yield list(zip(aa, reversed(bb), strict=False))


def main():
    for data in combine(gen(1, 2, 3, 4), gen(1, 2, 3, 4)):
        print(data)


if __name__ == "__main__":
    main()
