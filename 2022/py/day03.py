import numpy as np

x = np.genfromtxt('../../input/2022/day03.txt', dtype='str')

value = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def p1(x):
    score = 0

    for line in x:
        half = len(line)//2

        a, b = line[:half], line[half:]
        c = set(a) & set(b)
        score += value.index(next(iter(c)))

    return score


def p2(x):
    score = 0

    for i in range(len(x)//3):
        a, b, c = x[i*3], x[i*3+1], x[i*3+2]
        d = set(a) & set(b) & set(c)
        score += value.index(next(iter(d)))

    return score


print(p1(x))
print(p2(x))