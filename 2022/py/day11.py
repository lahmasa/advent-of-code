import numpy as np
from math import prod


def parse_monkey(lines):
    return {
        'items': [int(x) for x in lines[1][18:].split(',')],
        'op': lambda old: eval(lines[2][19:]),
        'test': lambda x: x % int(lines[3][21:]) == 0,
        'testnum': int(lines[3][21:]),
        'throw': {
            True: int(lines[4][29:]),
            False: int(lines[5][29:]),
        },
    }



def p1(filename):
    f = open(filename, 'r')
    monkeys = [parse_monkey(m.splitlines()) for m in f.read().split('\n\n')]
    ins = np.zeros(len(monkeys))
    
    for i in range(20):
        for i, m in enumerate(monkeys):
            for item in m['items']:
                ins[i] += 1
                new = m['op'](item) // 3
                test = m['test'](new)
                throw = m['throw'][test]
                monkeys[throw]['items'].append(new)
            monkeys[i]['items'] = []
            
    ins[::-1].sort()
    return int(ins[0]*ins[1])


def p2(filename):
    f = open(filename, 'r')
    monkeys = [parse_monkey(m.splitlines()) for m in f.read().split('\n\n')]
    ins = np.zeros(len(monkeys))
    mod = prod(m['testnum'] for m in monkeys)

    for i in range(10000):
        for i, m in enumerate(monkeys):
            for item in m['items']:
                ins[i] += 1
                new = m['op'](item) % mod
                test = m['test'](new)
                throw = m['throw'][test]
                monkeys[throw]['items'].append(new)
            monkeys[i]['items'] = []
            
    ins[::-1].sort()
    return int(ins[0]*ins[1])


filename = '../../input/2022/day11.txt'
print(p1(filename))
print(p2(filename))