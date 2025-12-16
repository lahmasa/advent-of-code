input_file = '../input/day02.txt'
with open(input_file) as f:
    data = f.read().strip().split(",")

############ first part ############

id_sum = 0

for d in data:
    l, u = d.split("-")
    # check if the number is a repeated pattern - split it in half and compare first and second half
    for n in range(int(l), int(u)+1):
        code = str(n)
        length = len(code)

        if (code[:length//2] == code[length//2:]):
            id_sum += n

print("The sum of all invalid IDs is:", id_sum)


############ second part ############

id_sum = 0

for d in data:
    l, u = d.split("-")
    # check if the number is a repeated pattern - split it in half and compare first and second half
    for n in range(int(l), int(u)+1):
        code = str(n)
        length = len(code)

        found_repetition = False

        for s in range(1, length//2+1):
            if length%s == 0 and found_repetition!=True:
                splits = length//s
                not_repeating = False

                if s == 1:
                    # check if they are all the same.
                    for comp in range(length-1):
                        if code[comp] != code[comp+1]:
                            not_repeating = True
                else:
                    for comp in range(s-1):
                        # if they are divisible by s, we need to do s-1 comparisons
                        if (code[splits*comp:splits*(comp+1)] != code[splits*(comp+1):splits*(comp+2)]):
                            not_repeating = True

                if(not_repeating==False):
                    found_repetition = True
                    id_sum += n

print("The sum of all invalid IDs is:", id_sum)
