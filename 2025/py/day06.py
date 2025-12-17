input_file = '../input/day06.txt'

# data = []
# with open(input_file) as f:
#     for line in f.read().splitlines():
#         data.append([i for i in line.split(" ") if i])

# total = 0
# for i in range(len(data[0])):
#     res = int(data[0][i])
#     op = data[4][i]

#     for j in range(3):
#         if op=='+':
#             res+=int(data[1+j][i])
#         else:
#             res*=int(data[1+j][i])

#     total += res

# print('Total is:', total)


############# second part ##########
# now, the columns must be read vertically

data = []
ops = []
with open(input_file) as f:
    *nums_lines, ops_line, _ = f.read().split("\n")

data = [[i, x] for i,x in enumerate(ops_line) if x in {'*', '+'}]

starts = [x[0] for x in data]
ops = [x[1] for x in data]
ends = [x-1 for x in starts[1:]] + [len(ops_line)]

nums = [[line[start:end] for line in nums_lines] for start,end in zip(starts,ends)]

total = 0
for i in range(len(nums)):
    res = int(nums[i][0])
    op = ops[i]

    for j in range(3):
        if op=='+':
            res+=int(nums[i][1+j])
        else:
            res*=int(nums[i][1+j])

    total+=res

print('Total is:', total)

############# second part ##########
# now, the columns must be read vertically

total = 0
for i in range(len(nums)):
    num = ends[i]-starts[i]
    cols = ['' for _ in range(num)]
    rows = nums[i]
    op = ops[i]

    for row in rows:
        for k, ch in enumerate(row):
            cols[k] += '' if ch==' ' else ch

    ## now we have the rows
    res = int(cols[0])
    for j in range(num-1):
        if op=='+':
            res+=int(cols[j+1])
        else:
            res*=int(cols[j+1])
        print(j, 'adding', cols[j+1])
    print(i, cols, op)
    total+=res

print('Total is:', total)
