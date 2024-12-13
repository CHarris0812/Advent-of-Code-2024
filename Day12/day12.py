grid = []
f = open("Day12/input.txt")
for line in f:
    line = line.replace("\n", "")
    grid.append([i for i in line])


visited = [[False for i in grid[0]] for j in grid]

def valid(a):
    if a[0] < 0 or a[0] >= len(grid) or a[1] < 0 or a[1] >= len(grid[0]):
        return False
    return True

def getAdjacents(r, c):
    return [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

def visit(r, c):
    area = 0
    p = 0
    plant = grid[r][c]
    frontier = [(r, c)]
    while len(frontier) > 0:
        cur = frontier.pop(-1)
        if not visited[cur[0]][cur[1]]:
            visited[cur[0]][cur[1]] = True
            area += 1
            adj = getAdjacents(cur[0], cur[1])
            for a in adj:
                if not valid(a) or grid[a[0]][a[1]] != plant:
                    p += 1
                else:
                    frontier.append(a)
    return area * p


count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not visited[i][j]:
            count += visit(i, j)
print(count)


visited = [[False for i in grid[0]] for j in grid]

def good(r, c, p):
    if not valid((r, c)) or grid[r][c] != p:
        return False
    return True

def corner(r, c, p):
    count = 0
    goodArr = [[good(r + j, c + i, p) for i in range(-1, 2)] for j in range(-1, 2)]

    stuff = [
        [(0, 0), (1, 0), (0, 1)],
        [(0, 2), (0, 1), (1, 2)],
        [(2, 0), (2, 1), (1, 0)],
        [(2, 2), (1, 2), (2, 1)]
    ]
    
    for i in stuff:
        if not goodArr[i[0][0]][i[0][1]]:
            if goodArr[i[1][0]][i[1][1]] and goodArr[i[2][0]][i[2][1]]:
                count += 1
        if not goodArr[i[1][0]][i[1][1]] and not goodArr[i[2][0]][i[2][1]]:
            count += 1
    return count
            


def visit2(r, c):
    area = 0
    plant = grid[r][c]
    frontier = [(r, c)]
    corners = 0
    while len(frontier) > 0:
        cur = frontier.pop(-1)
        if not visited[cur[0]][cur[1]]:
            visited[cur[0]][cur[1]] = True

            corners += corner(cur[0], cur[1], plant)

            area += 1
            adj = getAdjacents(cur[0], cur[1])
            for a in adj:
                if not valid(a) or grid[a[0]][a[1]] != plant:
                    pass
                else:
                    frontier.append(a)


    return area * corners



c = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not visited[i][j]:
            x = visit2(i, j)
            c += x
            print(x)
print(c)