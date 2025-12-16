input_file = '../input/day03.txt'
with open(input_file) as f:
    data = f.read().strip().split("\n")


########### first part ########

joltage = 0

for bank in data:
    first = max(bank[:-1])
    second = max(bank[bank.index(first)+1:])

    joltage += int(first + second)

print('Maximum joltage:', joltage)


########### second part #########

# now we need to turn on 12 batteries!!
joltage = 0

for bank in data:
    max_bank = ''
    current_bank = bank

    for s in range(12, 0, -1):
        length = len(current_bank)
        first = max(current_bank[:length-(s-1)])
        current_bank = current_bank[current_bank.index(first)+1:]
        max_bank += first

    joltage += int(max_bank)


print('Maximum joltage:', joltage)