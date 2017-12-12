#!/usr/bin/env python3

import argparse
from math import sqrt, ceil, floor
from urllib.request import urlopen

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='program input', type=int)

    return parser.parse_args()


def _solve_first(ipt):
    row_len = ceil(sqrt(ipt))
    mid_row = floor(row_len / 2)
    max_num = row_len ** 2

    dist_from_end = max_num - ipt
    dist_from_row_mid = abs(dist_from_end - mid_row)

    return dist_from_row_mid + mid_row


def _solve_second(ipt):
    integer_sequence= urlopen('https://oeis.org/A141481/b141481.txt').readlines()
    filtered_int_seq = filter(lambda v: b'#' not in v and not v.strip() == b'', integer_sequence)
    return min([int(y) for y in [x.split()[1] for x in filtered_int_seq] if ipt < int(y)])


def main():
    args = _parse_args()

    print('Part One:', _solve_first(args.input))
    print('Part Two:', _solve_second(args.input))

if __name__ == '__main__':
    main()
