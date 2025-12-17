input_file = '../input/day04.txt'

fk = []
with open(input_file) as f:
    data = f.read().strip().split("\n")

    for line in data:
        fk.append(line)

######### first part ###########

access = 0
rows, cols = len(fk), len(fk[0])

for i in range(rows):
    for j in range(cols):

        if fk[i][j] != '@':
            continue

        # start at zero
        adj = 0

        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                r = i + m
                c = j + n

                if 0 <= r < rows and 0 <= c < cols:
                    adj += (fk[r][c]=='@')
        
        # zero-zero is counted.
        if adj < 5:
            access += 1

print('Number of accessible forklifts:', access) # 1578


########### second part ############

rolls = 0  # total roll picked up
access = 100    # start at a nonzero value
fk = [list(row) for row in fk]

while access!=0:
    access = 0   # 

    # go another round
    for i in range(rows):
        for j in range(cols):

            if fk[i][j] != '@':
                continue

            # start at zero
            adj = 0

            for m in [-1, 0, 1]:
                for n in [-1, 0, 1]:
                    if m == 0 and n == 0:
                        continue 

                    r = i + m
                    c = j + n

                    if 0 <= r < rows and 0 <= c < cols:
                        adj += (fk[r][c]=='@')
            
            if adj < 4:
                access += 1
                fk[i][j] = 'x'

    rolls += access
    print('In this round we collected', access, 'rolls of paper for a total of', rolls)

print('Number of accessible rolls:', rolls) # 1578