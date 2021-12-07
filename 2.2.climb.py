#!/usr/bin/env python

from day2_part1_sail import iter_input
from dataclasses import dataclass

@dataclass
class SubmarineLocation:
    aim: int
    posx: int
    depth: int

location = SubmarineLocation(0, 0, 0)


def move(direction, ordinal):
    if direction == 'forward':
        location.posx += ordinal
        location.depth = max(0, location.depth + (location.aim * ordinal))
    elif direction == 'down':
        location.aim += ordinal
    elif direction == 'up':
        location.aim -= ordinal


def locate(commands):
    for direction, ordinal in commands:
        move(direction, ordinal)
        #print(f'{direction} {ordinal} > {location.posx}, {location.depth}') 
    return location.posx * location.depth

if __name__ == '__main__':
    print(locate(iter_input()))
