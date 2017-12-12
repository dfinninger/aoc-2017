#!/usr/bin/env python3

import argparse


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='program input')

    return parser.parse_args()


def _solve_first(ipt):
    chars = list(str(ipt))

    accum = 0
    for item in enumerate(chars):
        if item[1] == chars[item[0]-1]:
            accum += int(item[1])

    return accum


def _solve_second(ipt):
    chars = list(str(ipt))

    accum = 0
    for item in enumerate(chars):
        idx = (item[0] + len(chars) // 2) % len(chars)
        if item[1] == chars[idx]:
            accum += int(item[1])

    return accum


def main():
    args = _parse_args()

    ans1 = _solve_first(args.input)
    ans2 = _solve_second(args.input)

    print('Part One:', ans1)
    print('Part Two:', ans2)

if __name__ == '__main__':
    main()
