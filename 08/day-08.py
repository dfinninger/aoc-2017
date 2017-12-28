#!/usr/bin/env python3

import argparse
from collections import defaultdict, namedtuple
import re
import operator

Instruction = namedtuple('Instruction', ['register', 'incdec', 'value', 'condreg', 'oper', 'compint'])


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='program input')

    return parser.parse_args()


def _op(comp, a, b):
    return {'<': lambda: operator.lt(a, b),
            '>': lambda: operator.gt(a, b),
            '==': lambda: operator.eq(a, b),
            '>=': lambda: operator.ge(a, b),
            '<=': lambda: operator.le(a, b),
            '!=': lambda: operator.ne(a, b),
            'inc': lambda: operator.add(a, b),
            'dec': lambda: operator.sub(a, b),
            }[comp]()


def _parse_instr(instr):
    m = re.fullmatch(
            r'(?P<reg>\w+) (?P<incdec>\w+) (?P<val>[\w-]+) if (?P<condreg>\w+) (?P<oper>[><=!]+) (?P<compint>[\w-]+)', 
            instr)
    instr = Instruction(
                m.group('reg'),
                m.group('incdec'),
                int(m.group('val')),
                m.group('condreg'),
                m.group('oper'),
                int(m.group('compint')))

    return instr


def _exec_instr(reg_table, instr):
    if _op(instr.oper, reg_table[instr.condreg], instr.compint):
        new_val = _op(instr.incdec, reg_table[instr.register], instr.value)
        reg_table['max_ever'] = max(reg_table['max_ever'], new_val)
        reg_table[instr.register] = new_val

    return reg_table



def _solve_first(ipt):
    reg_table = defaultdict(lambda: 0)
    for line in ipt:
        instr = _parse_instr(line)
        reg_table = _exec_instr(reg_table, instr)

    del reg_table['max_ever']
    return max(reg_table.values())


def _solve_second(ipt):
    reg_table = defaultdict(lambda: 0)
    for line in ipt:
        instr = _parse_instr(line)
        reg_table = _exec_instr(reg_table, instr)

    return reg_table['max_ever']


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
