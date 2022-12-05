import numpy as np

x = np.genfromtxt('../../input/2022/day04.txt', dtype='str')

def p1(x):
    score = 0

    for line in x:
        a, b = line.split(',')

        a1, a2 = a.split('-')
        b1, b2 = b.split('-')

        if ((float(a1) >= float(b1)) & (float(a2) <= float(b2))) or (
            (float(a1) <= float(b1)) & (float(a2) >= float(b2))):
            score += 1

    return score


def p2(x):
    score = 0

    for line in x:
        a, b = line.split(',')

        a1, a2 = a.split('-')
        b1, b2 = b.split('-')

        c = set(np.arange(int(a1), int(a2)+1))
        d = set(np.arange(int(b1), int(b2)+1))

        if len(c & d) > 0:
            score += 1

    return score


print(p1(x))
print(p2(x))