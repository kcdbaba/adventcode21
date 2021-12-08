#!/usr/bin/env python

from itertools import tee

def iter_input():
    with open('inputs/day3') as f:
        for line in f:
            yield int(line, 2)


class Tree:
    def __init__(self, count=None):
        self.children = [None, None]
        self.count = count

    def __str__(self, id='head', level=0):
        ret = 'root' if level == 0 else repr(id) + ':' + repr(self.count)
        is_leaf = all(x is None for x in self.children)
        ret += '\n' if is_leaf else '\t'

        for idx in range(2):
            if self.children[idx] is not None:
                ret += ('\t'*(level+1) if ret.endswith('\n') else '')
                ret += self.children[idx].__str__(idx, level+1)
        return ret
    
    def add_child_bit(self, bit):
        if self.children[bit] is None:
            self.children[bit] = Tree(0)
        self.children[bit].count += 1


def count_bits(iter, digits=12):
    bit_count_tree = Tree()
    for binary in iter:
        curr = bit_count_tree
        for place in range(digits-1, -1, -1):
            bit = (binary & 2 ** place) >> place
            curr.add_child_bit(bit)
            curr = curr.children[bit]
    return bit_count_tree


def oxy_rating(tree):
    oxy = []
    while any(tree.children):
        bit = max([1,0], key=lambda x:(tree.children[x].count if tree.children[x] else 0))
        oxy.append(bit)
        tree = tree.children[bit]
    return int(''.join([str(x) for x in oxy]), 2)


def co2_rating(tree):
    co2 = []
    while any(tree.children):
        bit = min((x for x in (0,1) if tree.children[x] is not None), key=lambda x:tree.children[x].count)
        co2.append(bit)
        tree = tree.children[bit]
    return int(''.join([str(x) for x in co2]), 2)


def life_support_rating(tree):
    return oxy_rating(tree) * co2_rating(tree)

if __name__ == '__main__':
    bit_tree = count_bits(iter_input())
    print(life_support_rating(bit_tree))
