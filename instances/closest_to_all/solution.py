#!/usr/bin/env python

"""
for notation:
N - number of squares on the board
P - number of people

efficient solution:
first calculate the shortest path of each person to each square
(create matrix per person) and then calculate the square which is
the best. If several squares have the same value - print them all.

Complexity: P*N (to calculate the minimums for all people) and
another N*P to find the locations. Which is N*P

A less efficient solution would be one driven from the locations.
Pass over each location on the map calculating the mininum number
of steps each person has to get to get to it. Remember the sum
of all minimums.

Complexity: To calculate the minimum for every location its N.
We do that for every person P and for every square N. So we get
N*P*N = N^2*P

We code the more efficient solution here.
"""
import math  # for inf

# should we do debugging?
do_debug = False



class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, p):
        self.x += p.x
        self.y += p.y

    def __str__(self):
        return f"({self.x},{self.y})"


directions = [
    Position(0, 1),
    Position(1, 0),
    Position(0, -1),
    Position(-1, 0),
]


class Matrix:
    def __init__(self, v, w, h):
        self.data = [[v for _ in range(w)] for _ in range(h)]
        self.w = w
        self.h = h

    def get(self, x, y):
        return self.data[y][x]

    def get_pos(self, p) -> int:
        return self.data[p.y][p.x]

    def set(self, x, y, v):
        self.data[y][x] = v

    def set_pos(self, p, v):
        self.data[p.y][p.x] = v

    def illegal(self, x, y):
        return x < 0 or x >= self.w or y < 0 or y >= self.h

    def illegal_pos(self, p):
        return p.x < 0 or p.x >= self.w or p.y < 0 or p.y >= self.h

    def add(self, m):
        for y, row in enumerate(self.data):
            for x, _e in enumerate(row):
                if m.get(x, y) is not None and _e is not None:
                    row[x] += m.get(x, y)

    def minimum(self):
        val = math.inf
        for row in self.data:
            for e in row:
                if e is not None and e < val:
                    val = e
        return val

    def duplicate(self):
        m = Matrix(None, self.w, self.h)
        for y, row in enumerate(self.data):
            for x, e in enumerate(row):
                m.set(x, y, e)
        return m

    def print(self):
        for row in self.data:
            for e in row:
                print(e, end="")
            print()

    def __str__(self):
        res = ""
        for row in self.data:
            for e in row:
                res += str(e) + ", "
            res += "\n"
        return res

    @staticmethod
    def from_strings(m):
        s = Matrix(" ", len(m[0]), len(m))
        for y, row in enumerate(m):
            for x, c in enumerate(row):
                s.set(x, y, c)
        return s


def solve(m):
    # first find all the people in the matrix
    people = []
    for y in range(m.h):
        people.extend(Position(x, y) for x in range(m.w) if m.get(x, y) == "P")
    assert len(people) > 0
    # now calculate shortest distance per person
    sdms = []
    for p in people:
        sdm = Matrix(math.inf, m.w, m.h)
        sdm.set_pos(p, 0)
        positions = [p]
        while len(positions) > 0:
            pos = positions.pop()
            steps = sdm.get_pos(pos)
            for d in directions:
                cpos = Position(pos.x, pos.y)
                cpos.add(d)
                if sdm.illegal_pos(cpos):
                    continue
                place = m.get_pos(cpos)
                if place == "*":
                    continue
                cval = sdm.get_pos(cpos)
                if cval is not None:
                    if steps + 1 < cval:
                        sdm.set_pos(cpos, steps + 1)
                    else:
                        continue
                else:
                    sdm.set_pos(cpos, steps + 1)
                positions.append(cpos)
        if do_debug:
            print(sdm)
        sdms.append(sdm)
    # now find the ideal position for the kitchen
    sums = sdms[0].duplicate()
    for sdm in sdms[1:]:
        sums.add(sdm)
    if do_debug:
        print(sums)
    # now find the minimum and convert to a matrix of results...
    mini = sums.minimum()
    if do_debug:
        print(mini)
    # create a boolean matrix showing the solutions
    results = Matrix("_", sums.w, sums.h)
    for x in range(sums.w):
        for y in range(sums.h):
            if sums.get(x, y) == mini and mini != math.inf:
                results.set(x, y, "*")
    print("question")
    m.print()
    print("answer")
    results.print()


#########
# tests #
#########
m1 = [
    "P___P",
    "_____",
    "_____",
    "_____",
    "P___P",
]
solve(Matrix.from_strings(m1))

m2 = [
    "P___P",
    "_*_*_",
    "_*_*_",
    "_***_",
    "P___P",
]
solve(Matrix.from_strings(m2))

m3 = [
    "P*__P",
    "_*___",
    "_*___",
    "_*___",
    "P___P",
]
solve(Matrix.from_strings(m3))

m4 = [
    "P*__P",
    "_*___",
    "_*___",
    "_*___",
    "P*__P",
]
solve(Matrix.from_strings(m4))

m5 = [
    "P___P",
    "_____",
    "_____",
    "_____",
    "____P",
]
solve(Matrix.from_strings(m5))

m6 = [
    "P___P",
    "_____",
    "___**",
    "_____",
    "____P",
]
solve(Matrix.from_strings(m6))

m7 = [
    "P____________P",
]
solve(Matrix.from_strings(m7))

m8 = [
    "P_____________",
    "________P_____",
]
solve(Matrix.from_strings(m8))
