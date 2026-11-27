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
        self.inset = [True] * n
        self.succ: list[int | None] = list(range(n))

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
        return rj

    # methods for this exercise
    def successor(self, i: int):
        if self.inset[i]:
            return i
        r = self.find_root(i)
        return self.succ[r]

    def remove(self, i: int) -> None:
        self.inset[i] = False
        if i + 1 < self.n:
            if not self.inset[i + 1]:
                s = self.successor(i + 1)
                r = self.union(i, i + 1)
                self.succ[r] = s
            else:
                self.succ[i] = i + 1
        else:
            self.succ[i] = None
        if i - 1 >= 0 and not self.inset[i - 1]:
            s = self.successor(i)
            r = self.union(i, i - 1)
            self.succ[r] = s

    def print(self) -> None:
        print(self.root)
        print(self.inset)
        print(self.succ)

    def print_short(self) -> None:
        print(self.inset)
        print([self.successor(i) for i in range(self.n)])


def main() -> None:
    s = Algo(15)
    s.print_short()
    s.remove(10)
    s.print_short()
    s.remove(5)
    s.print_short()
    s.remove(11)
    s.print_short()
    s.remove(9)
    s.print_short()
    s.remove(12)
    s.remove(13)
    s.remove(14)
    s.print_short()


if __name__ == '__main__':
    main()
