import numpy as np


file = open('day1.txt')

max = np.zeros(3)
score = 0

for line in file:
    if line != '\n':
        score += int(line)

    else:
        if score >= max[0]:
            max[2] = max[1]
            max[1] = max[0]
            max[0] = score
        
        elif score >= max[1]:
            max[2] = max[1]
            max[1] = score
        
        elif score >= max[2]:
            max[2] = score

        score = 0

print(max)
print(max[0]+max[1]+max[2])

    