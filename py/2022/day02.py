def p1(f):
    score = 0

    for line in f:
        i, j = line.split()
        
        a = 'ABC'.index(i)
        b = 'XYZ'.index(j)

        score += b + 1

        x = (b - a) % 3
        if x == 0:
            score += 3
        elif x == 1:
            score += 6
    
    return score


def p2(f):
    score = 0

    for line in f:
        i, j = line.split()

        a = 'ABC'.index(i)
        b = 'XYZ'.index(j)

        score += b * 3

        if b == 0:
            score += (a - 1) % 3 + 1
        elif b == 1:
            score += a + 1
        else:
            score += (a + 1) % 3 + 1

    return score

f = open('../../input/2022/day02.txt')
print(p2(f))
