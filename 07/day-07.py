#!/usr/bin/env python3

import argparse
import re
from collections import Counter

class Disc:
    def __init__(self, name, weight, parent=None, children=None):
        self._name = name
        self._weight = weight
        self._parent = parent
        self._children = children

    def __repr__(self):
        return f'Disc({self._name}, {self._weight})'

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = children


def _disc_from_input(instr):
    m = re.fullmatch(r'(\w+) \((\d+)\)( -> (.*))?', instr)
    try:
        return Disc(m.group(1), int(m.group(2)), children=[x.strip() for x in m.group(4).split(',')])
    except AttributeError:
        return Disc(m.group(1), int(m.group(2)))


def _populate_disc_tree(ipt):
    discs = {}
    for i in ipt:
        d = _disc_from_input(i)
        discs[d.name] = d

    for _, disc in discs.items():
        if disc.children:
            disc.children = [discs[child] for child in disc.children]
            for child in disc.children:
                child.parent = disc

    return discs


def _get_tree_root(discs):
    parentless_discs = [d for _, d in discs.items() if not d.parent]
    return parentless_discs[0]


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='program input')

    return parser.parse_args()


def _solve_first(ipt):
    discs = _populate_disc_tree(ipt)
    return _get_tree_root(discs).name
            

def _child_weights(disc):
    if disc.children:
        weights = [_child_weights(disc) for disc in disc.children]
        if len(set(weights)) > 1:
            print('---')
            for i, child in enumerate(disc.children):
                print(f'{child.name}: {weights[i]} ({child.weight} : {[c.weight for c in child.children]})')
        return disc.weight + sum(weights)
    else:
        return disc.weight


def _solve_second(ipt):
    discs = _populate_disc_tree(ipt)
    root = _get_tree_root(discs)
    _child_weights(root)
    return "You'll need to use the above table to firgure it out, cleaning up the above output is hard."


def main():
    args = _parse_args()

    if args.input:
        in_data = args.input
    else:
        with open('input.txt') as f:
            in_data = f.read()

    in_data = in_data.splitlines()

    print('Part One:', _solve_first(in_data))
    print('Part Two:', _solve_second(in_data))

if __name__ == '__main__':
    main()
