def p1(filename):
    x = open(filename, 'r')
    grid = x.read().splitlines()

    ans = 0

    for ti, row in enumerate(grid):
        for tj, tree in enumerate(row):
            ans += (
                all(grid[ti][j] < tree for j in range(0, tj))
                or all(grid[ti][j] < tree for j in range(tj+1, len(row)))
                or all(grid[i][tj] < tree for i in range(0, ti))
                or all(grid[i][tj] < tree for i in range(ti+1, len(grid)))
            )

    return ans


def p2(filename):
    x = open(filename, 'r')
    grid = x.read().splitlines()

    ans = 0

    for ti, row in enumerate(grid):
        for tj, tree in enumerate(row):
            left = min(((tj-j) for j in range(0, tj) if grid[ti][j] >= tree), default=tj)
            right = min(((j-tj) for j in range(tj+1, len(row)) if grid[ti][j] >= tree), default=len(row)-tj-1)
            up = min(((ti-i) for i in range(0, ti) if grid[i][tj] >= tree), default=ti)
            down = min(((i-ti) for i in range(ti+1, len(grid)) if grid[i][tj] >= tree), default=len(grid)-ti-1)

            view = left * right * up * down
            
            if view > ans:
                ans = view                

    return ans


filename = '../../input/2022/day08.txt'
print(p1(filename))
print(p2(filename))

