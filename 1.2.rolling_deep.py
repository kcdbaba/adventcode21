#!/usr/bin/env python

from itertools import tee
from day1_part1_sinks import iter_input


def pairwise_lagged(iter, lag=1):
    slow, fast = tee(iter)
    for _ in range(lag):
        next(fast, None)
    return zip(slow, fast)


def count_deeper_steps():
    count = 0
    for prev, depth in pairwise_lagged(iter_input(), lag=3):
        if depth > prev:
            count += 1
    return count


if __name__ == '__main__':
    print(count_deeper_steps())
