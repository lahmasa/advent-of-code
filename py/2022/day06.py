def p1(filename):
    x = open(filename, 'r').read()

    for i in range(4, len(x)):
        if len(set(x[i-4:i])) == 4:
            return i


def p2(filename):
    x = open(filename, 'r').read()

    for i in range(14, len(x)):
        if len(set(x[i-14:i])) == 14:
            return i


filename = '../../input/2022/day06.txt'
print(p1(filename))
print(p2(filename))