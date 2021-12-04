#!/usr/bin/env python

from itertools import tee

def iter_input():
    with open('inputs/day1') as f:
        for line in f:
            yield int(line)


def pairwise(iter):
    slow, fast = tee(iter)
    next(fast, None)
    return zip(slow, fast)


def count_deeper_steps():
    count = 0
    for prev, depth in pairwise(iter_input()):
        if depth > prev:
            count += 1
    return count


if __name__ == '__main__':
    print(count_deeper_steps())
