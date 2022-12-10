import numpy as np


def p1(filename):
    f = open(filename, 'r')

    dirs = {'R': np.array((1, 0)),
            'L': np.array((-1, 0)),
            'U': np.array((0, 1)),
            'D': np.array((0, -1))}

    h = [0, 0]
    t = [0, 0]
    pos = set()

    for line in f.read().splitlines():
        dir, steps = line.split()
        step = dirs[dir]

        for i in range(int(steps)):
            h += step

            if abs(h[0] - t[0]) > 1 or \
               abs(h[1] - t[1]) > 1:
                t += np.sign(h-t)

            pos.add(tuple(t))

    return len(pos)


def p2(filename):
    f = open(filename, 'r')

    dirs = {'R': np.array((1, 0)),
            'L': np.array((-1, 0)),
            'U': np.array((0, 1)),
            'D': np.array((0, -1))}

    ht = [[0, 0] for i in range(10)]
    pos = set()

    for line in f.read().splitlines():
        dir, steps = line.split()
        step = dirs[dir]

        for i in range(int(steps)):
            ht[0] += step

            for j in range(1, len(ht)):
                h = ht[j-1]
                t = ht[j]

                if abs(h[0] - t[0]) > 1 or \
                   abs(h[1] - t[1]) > 1:
                    ht[j] += np.sign(h-t)

            pos.add(tuple(ht[len(ht)-1]))

    return len(pos)


filename = 'day09.txt'
print(p1(filename))
print(p2(filename))
