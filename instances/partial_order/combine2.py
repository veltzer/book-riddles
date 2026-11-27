#!/usr/bin/env python

"""
Combine 2
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


def gen(*data: object):
    yield from data


def append_next_or_drop(a: Generator[object], aa: list[object], bb: list[object]) -> None:
    try:
        aa.append(next(a))  # either append one new item to aa...
    except StopIteration:
        a.close()  # This may be called more than once --- but this is ok.
        bb.pop(0)  # or pop of the first element of bb.


def combine(a: Generator[object], b: Generator[object]):
    aa: list[object] = []
    bb: list[object] = []
    while True:
        append_next_or_drop(a, aa, bb)
        append_next_or_drop(b, bb, aa)
        if len(aa) == 0:
            break
        yield list(zip(aa, reversed(bb), strict=False))


def main() -> None:
    for data in combine(gen(1, 2, 3, 4), gen(1, 2, 3, 4)):
        print(data)


if __name__ == "__main__":
    main()
