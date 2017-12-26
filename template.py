#!/usr/bin/env python3

import argparse


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='program input')

    return parser.parse_args()


def _solve_first(ipt):
	pass


def _solve_second(ipt):
	pass


def main():
    args = _parse_args()

    if args.input:
        in_data = args.input
    else:
        with open('input.txt') as f:
            in_data = f.read()

    print('Part One:', _solve_first(in_data))
    print('Part Two:', _solve_second(in_data))

if __name__ == '__main__':
    main()
