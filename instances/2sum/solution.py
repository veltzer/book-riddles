#!/usr/bin/env python

"""
Solution
"""

def sums_to_target(data: list[int], k: int) -> bool:
    data.sort()
    lhs = 0
    rhs = len(data) - 1
    while lhs < rhs:
        current_sum = data[lhs] + data[rhs]
        if current_sum == k:
            return True
        if current_sum < k:
            lhs += 1
        else:
            rhs -= 1
    return False


def all_pairs(data: list[int], k: int):
    data.sort()
    lhs = 0
    rhs = len(data) - 1
    results = []
    while lhs < rhs:
        current_sum = data[lhs] + data[rhs]
        if current_sum == k:
            results.append((data[lhs], data[rhs]))
            lhs += 1
            rhs -= 1
        elif current_sum < k:
            lhs += 1
        else:
            rhs -= 1
    return results


def main() -> None:
    data = [2 ** x for x in range(10)]
    print(data)
    for i in range(10):
        print(i, sums_to_target(data, i))

    data = list(range(10))
    print(data)
    for i in range(10):
        print(i, all_pairs(data, i))


if __name__ == "__main__":
    main()
