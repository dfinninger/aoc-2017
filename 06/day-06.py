#!/usr/bin/env python3

import argparse


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='program input')

    return parser.parse_args()


def _solve_first(ipt):
    found_configs = []
    
    current = ipt
    accum = 0

    while current not in found_configs:
        found_configs.append(current.copy())
        accum += 1
        current = _redistribute(current)

    return accum


def _redistribute(lst):
    max_item = max(lst)
    index = lst.index(max_item)
    lst[index] = 0
    
    for i in range(max_item):
        idx = (i + index + 1) % len(lst)
        lst[idx] += 1

    return lst


def _solve_second(ipt):
    found_configs = []
    
    current = ipt
    accum = 0

    # pre-populate
    while current not in found_configs:
        found_configs.append(current.copy())
        current = _redistribute(current)

    found_configs.clear()
    while current not in found_configs:
        found_configs.append(current.copy())
        accum += 1
        current = _redistribute(current)

    return accum


def main():
    args = _parse_args()

    if args.input:
        in_data = args.input
    else:
        with open('input.txt') as f:
            in_data = f.read()

    in_data = [int(i) for i in in_data.split()]

    print('Part One:', _solve_first(in_data))
    print('Part Two:', _solve_second(in_data))

if __name__ == '__main__':
    main()
