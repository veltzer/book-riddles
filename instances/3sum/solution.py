#!/usr/bin/env python

"""
Solution
"""

def three_loops(data):
    """ this is n^3 complexity """
    results = []
    for p1, x1 in enumerate(data):
        for p2, x2 in enumerate(data[p1 + 1:]):
            for x3 in data[p1 + p2 + 2:]:
                if x1 + x2 == x3:
                    results.append((x1, x2, x3))
                if x2 + x3 == x1:
                    results.append((x1, x2, x3))
                if x1 + x3 == x2:
                    results.append((x1, x2, x3))
    results.sort()
    return results


def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:  # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        if target > val:
            if lower == x:  # this two are the actual lines
                break  # youre looking for
            lower = x
        if target < val:
            upper = x
    raise ValueError("shouldnt be here")


def two_loops_and_binary(data):
    """ this is n^2*log(n) complexity """
    results = []
    s_data = sorted(data)
    for p1, x1 in enumerate(s_data):
        results.extend(
            (x1, x2, x1 + x2)
            for x2 in s_data[p1 + 1:]
            if binary_search(s_data, x1 + x2) is not None
        )
    results.sort()
    return results


def using_hash(data):
    """ the idea here is to put all the elements of the data array in a
    hash table (O(n*log(n)) or O(n) in the average case) and then do a O(n^2)
    double loop and check for each pair if they sum up to the third.
    """
    results = []
    s = set(data)
    for p1, x1 in enumerate(data):
        results.extend((x1, x2, x1 + x2) for x2 in data[p1 + 1:] if x1 + x2 in s)
    results.sort()
    return results


def pointers_going_inward(data):
    """ this is n^2 complexity """
    # the sorting is n*log(n)
    s_data = sorted(data)
    n = len(s_data)
    results = []
    for i in range(n - 1, 1, -1):
        a = s_data[i]
        start = 0
        end = i - 1
        while start < end:
            b = s_data[start]
            c = s_data[end]
            if b + c == a:
                results.append((a, b, c))
                start = start + 1
                end = end - 1
            elif b + c < a:
                start = start + 1
            else:
                end = end - 1
    results.sort()
    return results


def main():
    data = [22, 1, 7, 2, 3, 19]
    print(data)
    # print(sorted(data))
    print(three_loops(data))
    print(two_loops_and_binary(data))
    print(using_hash(data))
    print(pointers_going_inward(data))


if __name__ == "__main__":
    main()
