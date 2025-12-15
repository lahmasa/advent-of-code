import numpy as np


def p1(filename):
    f = open(filename, 'r')
    x = 1

    t = 0
    ans = 0

    def tick():
        nonlocal ans, t

        t += 1
        if t in (20, 60, 100, 140, 180, 220):
            ans += t * x

    for line in f.read().splitlines():
        dir = line.split()

        tick()

        if dir[0] == 'addx':
            tick()
            x += int(dir[1])

    return ans



def p2(filename):
    f = open(filename, 'r')

    x = 1
    t = 0

    def tick():
        nonlocal t

        if t % 40 in np.arange(x-1, x+2):
            print('#', end='')
        else:
            print('.', end='')

        t += 1

        if t % 40 == 0:
            print()

    for line in f.read().splitlines():
        dir = line.split()

        tick()

        if dir[0] == 'addx':
            tick()
            x += int(dir[1])

    return print()


filename = '../../input/2022/day10.txt'
print(p1(filename))
print(p2(filename))
