from pathlib import Path
from collections import defaultdict


def p1(filename):
    x = open(filename, 'r')
    dir = Path('/')
    dict = defaultdict(int)

    for line in x.read().splitlines():
        inst = line.split()
        if inst[1] == 'cd':
            dir = dir / inst[2]
            dir = dir.resolve()
        
        elif inst[0].isdigit():
            size = int(inst[0])
            for path in [dir, *dir.parents]:
                dict[path] += size
            
    return sum(x for x in dict.values() if x <= 100000)


def p2(filename):
    x = open(filename, 'r')
    dir = Path('/')
    dict = defaultdict(int)

    for line in x.read().splitlines():
        inst = line.split()
        if inst[1] == 'cd':
            dir = dir / inst[2]
            dir = dir.resolve()
        
        elif inst[0].isdigit():
            size = int(inst[0])
            for path in [dir, *dir.parents]:
                dict[path] += size
            
    return min(x for x in dict.values() if dict[Path('/')] - x <= 70000000 - 30000000)


filename = '../../input/2022/day07.txt'
print(p1(filename))
print(p2(filename))