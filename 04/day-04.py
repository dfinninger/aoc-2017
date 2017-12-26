#!/usr/bin/env python3

import argparse
from collections import Counter


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='program input')

    return parser.parse_args()


def _solve_first(ipt):
    lines = ipt.splitlines()
    return sum(Counter(line.split()).most_common(1)[0][1] <= 1 for line in lines)


def _solve_second(ipt):
    counter = 0
    for line in ipt.splitlines():
        word_counters = [''.join(sorted(word)) for word in line.split()]
        if len(word_counters) == len(set(word_counters)):
            counter += 1

    return counter


def main():
    args = _parse_args()

    print('Part One:', _solve_first(args.input))
    print('Part Two:', _solve_second(args.input))

if __name__ == '__main__':
    main()
