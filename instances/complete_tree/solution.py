#!/usr/bin/env python

"""
recursive solution, not very efficient since it always scans the entire tree
its better to scan top to bottom to stop if one of the levels is not full but
this one will scan everything.
returns height, complete, last level full
"""


class Tree:
    def __init__(self):
        self.left: Tree | None = None
        self.right: Tree | None = None


def complete_tree_inter(t):
    if t is None:
        return 0, True, True
    (lh, _labl, llll) = complete_tree_inter(t.left)
    (rh, rabl, rlll) = complete_tree_inter(t.right)
    if lh < rh:
        return rh + 1, False, False
    if lh == rh:
        if llll:
            return rh + 1, rabl, rlll
        return rh + 1, False, False
    if lh == rh + 1:
        return lh + 1, rlll, False
    if lh > rh + 1:
        return lh + 1, False, False
    raise ValueError("shouldnt be here")


def complete_tree(t):
    return complete_tree_inter(t)[1]


def complete_tree_2_inter(s):
    """
    non recursive solution, better performance if implemented with efficient data structures
    input is
    """
    this_level_full = True
    saw_none = False
    saw_something_after_none = False
    have_next_level = False
    next_level = []
    for x in s:
        if x is None:
            this_level_full = False
            next_level.append(None)
            next_level.append(None)
            saw_none = True
        else:
            if saw_none:
                saw_something_after_none = True
            next_level.append(x.left)
            next_level.append(x.right)
            if x.left is not None or x.right is not None:
                have_next_level = True
    # this level is not complete
    if saw_something_after_none:
        return False
    if saw_none:
        return not have_next_level
    # this level is not full and have next level
    if this_level_full:
        if have_next_level:
            return complete_tree_2_inter(next_level)
        return True
    raise ValueError("shouldnt be here")


def complete_tree_2(t):
    s = [t]
    return complete_tree_2_inter(s)


#########
# tests #
#########
t1 = Tree()
assert complete_tree(t1)
assert complete_tree_2(t1)

t2 = Tree()
t2.left = Tree()
t2.right = Tree()
assert complete_tree(t2)
assert complete_tree_2(t2)

t3 = Tree()
t3.left = t2
t3.right = t2
assert complete_tree(t3)
assert complete_tree_2(t3)

t4 = Tree()
t4.right = t1
t4.left = Tree()
t4.left.left = t1
assert complete_tree(t4)
assert complete_tree_2(t4)

t5 = Tree()
t5.left = t2
t5.right = Tree()
t5.right.left = t1
assert complete_tree(t5)
assert complete_tree_2(t5)

t6 = Tree()
t6.left = t2
t6.right = Tree()
t6.right.right = t1
assert not complete_tree(t6)
assert not complete_tree_2(t6)

t7 = Tree()
t7.left = Tree()
t7.left.left = t1
t7.right = Tree()
t7.right.left = t1
assert not complete_tree(t7)
assert not complete_tree_2(t7)

t8 = Tree()
t8.left = t2
assert not complete_tree(t8)
assert not complete_tree_2(t8)
