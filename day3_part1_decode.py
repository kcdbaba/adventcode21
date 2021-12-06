#!/usr/bin/env python

from itertools import tee

def iter_input():
    with open('inputs/day3') as f:
        for line in f:
            yield int(line, 2)


def count_ones(iter, digits=12):
    count = 0
    ones = [0 for _ in range(digits)]
    for binary in iter:
        count += 1
        for place in range(digits):
            ones[place] += (binary & (2 ** place)) >> place
    return ones[::-1], count


def decode_power(digits=12):
    places_ones, readouts = count_ones(iter_input(), digits)
    gamma_bits = (''.join([('1' if (ones > readouts/2) else '0') for ones in places_ones]))
    gamma = int(gamma_bits, 2)
    epsilon = gamma ^ (2 ** digits - 1)
    return gamma * epsilon

if __name__ == '__main__':
    print(decode_power())
