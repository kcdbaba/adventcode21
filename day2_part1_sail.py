#!/usr/bin/env python


def iter_input():
    with open('inputs/day2') as f:
        for line in f:
            act, ord = line.strip().split(' ')
            yield (act, int(ord))



from dataclasses import dataclass

@dataclass
class SubmarineLocation:
    x: int
    depth: int

location = SubmarineLocation(0, 0)


def move(direction, distance):
    if direction == 'forward':
        location.x += distance
    elif direction == 'down':
        location.depth += distance
    elif direction == 'up':
        location.depth = max(0, location.depth - distance)


def locate(commands):
    for direction, distance in commands:
        move(direction, distance)
        #print(f'{direction} {distance} > {location.x}, {location.depth}') 
    return location.x * location.depth

if __name__ == '__main__':
    print(locate(iter_input()))
