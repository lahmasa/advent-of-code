import numpy as np
from collections import deque


def p1(filename):
    x = open(filename)
    crates, instructions = x.read().split("\n\n")
    stacks = []

    for line in crates.splitlines():     
        for i, ix in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            if line[ix] != ' ':
                stacks[i].append(line[ix])

    for inst in instructions.splitlines():
        x = inst.split(' ')
        
        for i in range(int(x[1])):
            stacks[int(x[5])-1].insert(0, stacks[int(x[3])-1].popleft())

    return "".join(x[0] for x in stacks)


def p2(x):
    x = open(filename)
    crates, instructions = x.read().split("\n\n")
    stacks = []

    for line in crates.splitlines():     
        for i, ix in enumerate(range(1, len(line), 4)):
            while i >= len(stacks):
                stacks.append(deque())
            if line[ix] != ' ':
                stacks[i].append(line[ix])

    for inst in instructions.splitlines():
        x = inst.split(' ')
        
        for i in range(int(x[1])):
            stacks[int(x[5])-1].insert(0, stacks[int(x[3])-1][int(x[1])-i-1])

        for i in range(int(x[1])):
            stacks[int(x[3])-1].popleft()


    return "".join(x[0] for x in stacks)


filename = '../../input/2022/day05.txt'
print(p1(filename))
print(p2(filename))