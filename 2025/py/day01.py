input_file = '../input/day01.txt'
with open(input_file) as f:
    data = f.read().strip().split("\n")

#### first part ####

dial=50
passw=0

for line in data:
    d, move = line[0], int(line[1:])
    dial += move if d=="R" else -move
    dial %= 100
    passw += dial == 0

print("First part:", passw)

#### second part ####

dial=50
passw=0

for line in data:
    d, move = line[0], int(line[1:])
    for _ in range(move):
        dial += 1 if d=="R" else -1
        dial %= 100
        passw += dial == 0

print("Second part:", passw)
