#!/usr/bin/env python3

import argparse


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='program input')

    return parser.parse_args()


def _solve_first(ipt):
    in_list = [int(i) for i in ipt.splitlines()]

    index = in_list[0]
    in_list[0] += 1
    accum = 0

    while True:
        accum += 1
        try:
            next_index = in_list[index] + index
            in_list[index] += 1
            index = next_index
        except IndexError:
            return accum


def _solve_second(ipt):
    in_list = [int(i) for i in ipt.splitlines()]

    index = in_list[0]
    in_list[0] += 1
    accum = 0

    while True:
        accum += 1
        try:
            next_index = in_list[index] + index
            if in_list[index] >= 3:
                in_list[index] -= 1
            else:
                in_list[index] += 1
            index = next_index
        except IndexError:
            return accum


def main():
    args = _parse_args()

    print('Part One:', _solve_first(args.input))
    print('Part Two:', _solve_second(args.input))


if __name__ == '__main__':
    main()
