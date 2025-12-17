input_file = '../input/day05.txt'

with open(input_file) as f:
    data = f.read().strip().split("\n\n")

    ranges = data[0].split("\n")
    ids = [int(i) for i in data[1].split("\n")]

freshness = []
for line in ranges:
    freshness.append([int(i) for i in line.split("-")])


###### parsed the data #####
fresh_items = 0

for j in range(len(ids)):
    fresh = False

    for i in range(len(freshness)):
        if (ids[j]>=freshness[i][0] and ids[j]<=freshness[i][1]):
            fresh=True
            break

    fresh_items += fresh

print('There are', fresh_items, 'fresh items.')


############# second part ###########

fresh_ids = 0
overlap = 0

freshness.sort()
merged = []

for j in range(len(freshness)):
    start, end = freshness[j]

    # either start a new range or extend the last one!
    if len(merged)==0 or merged[-1][1] < start-1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(end, merged[-1][1])  # replace the end

fresh_ids = sum((end+1 -start for start, end in merged))
print('Fresh ids:', fresh_ids)