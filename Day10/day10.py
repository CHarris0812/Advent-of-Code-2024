grid = []
f = open("Day10/input.txt")
for line in f:
    line = line.replace("\n", "")
    grid.append([int(i) for i in line])

def valid(r, c):
    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
        return True
    return False

def adjacents(r, c):
    a = []
    if valid(r - 1, c):
        a.append((r - 1, c))
    if valid(r + 1, c):
        a.append((r + 1, c))
    if valid(r, c - 1):
        a.append((r, c - 1))
    if valid(r, c + 1):
        a.append((r, c + 1))
    return a

def reachable(r, c):
    found = 0
    visited = set()
    frontier = [(r, c)]
    while len(frontier) > 0:
        cur = frontier.pop(-1)
        if cur not in visited:
            if grid[cur[0]][cur[1]] == 9:
                found += 1
            visited.add(cur)
            for i in adjacents(cur[0], cur[1]):
                if grid[i[0]][i[1]] == grid[cur[0]][cur[1]] + 1:
                    frontier.append((i[0], i[1]))
    return found


count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            count += reachable(i, j)
print(count)


def trailheads(r, c):
    found = 0
    visited = set()
    frontier = [((r, c), 0)]
    while len(frontier) > 0:
        cur = frontier.pop(-1)
        if cur not in visited:
            visited.add(cur)
            
            temp = cur
            cur = cur[0]
            if grid[cur[0]][cur[1]] == 9:
                found += 1
            
            for i in adjacents(cur[0], cur[1]):
                if grid[i[0]][i[1]] == grid[cur[0]][cur[1]] + 1:
                    new =  [(i[0], i[1])]
                    temp = new + list(temp)
                    frontier.append(tuple(temp))
    return found

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            count += trailheads(i, j)
print(count)