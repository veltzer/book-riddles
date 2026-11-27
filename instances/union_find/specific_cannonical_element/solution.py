#!/usr/bin/env python

"""
Solution
"""

class Algo:
    def __init__(self, n: int) -> None:
        self.n = n
        # standard union-find stuff
        self.root = list(range(n))
        # extra data for this exercise
        self.largest = list(range(n))

    # standard union-find methods
    def find_root(self, i: int):
        """returns the root"""
        while self.root[i] != i:
            i = self.root[i]
        return i

    def union(self, i: int, j: int):
        """returns the new root"""
        ri = self.find_root(i)
        rj = self.find_root(j)
        self.root[ri] = rj
        self.largest[rj] = max(self.largest[ri], self.largest[rj])
        return rj

    # methods for this exercise
    def find(self, i: int):
        r = self.find_root(i)
        return self.largest[r]

    def print(self) -> None:
        print('================================')
        print([self.find_root(i) for i in range(self.n)])
        print([self.find(i) for i in range(self.n)])
        print('================================')


s = Algo(15)
s.print()
s.union(10, 11)
s.print()
s.union(11, 12)
s.print()
s.union(12, 13)
s.print()
s.union(13, 14)
s.print()
s.union(2, 5)
s.union(5, 8)
s.print()
