#!/usr/bin/env python3

import argparse


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='program input')

    return parser.parse_args()


def _make_spreadsheet(ipt):
    return [[int(z) for z in y.split()]
            for y in ipt.splitlines()]


def _solve_first(spreadsheet):
    return sum([max(row) - min(row) for row in spreadsheet])


def _solve_second(spreadsheet):
    return sum([x // y
                for row in spreadsheet
                for x in row
                for y in row
                if not x == y and x % y == 0])


def main():
    args = _parse_args()

    spreadsheet = _make_spreadsheet(args.input)

    print('Part One:', _solve_first(spreadsheet))
    print('Part Two:', _solve_second(spreadsheet))

if __name__ == '__main__':
    main()
