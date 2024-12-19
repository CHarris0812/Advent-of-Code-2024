f = open("Day18/input.txt")
data = f.readlines()
data = [i.replace("\n", "") for i in data]
data = [i.split(",") for i in data]
data = [(int(i[1]), int(i[0])) for i in data]


SIZE = 71
grid = [["." for i in range(SIZE)] for j in range(SIZE)]

def valid(r, c):
    if r < 0 or r >= SIZE or c < 0 or c >= SIZE:
        return False
    return True

def getAdjacents(point):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    adj = []
    for i in dirs:
        if valid(point[0] + i[0], point[1] + i[1]):
            if grid[point[0] + i[0]][point[1] + i[1]] == ".":
                adj.append((point[0] + i[0], point[1] + i[1]))
    return adj


for i in range(1024):
    grid[data[i][0]][data[i][1]] = "#"

import heapq
q = [(0, 0, 0)]
heapq.heapify(q)



visited = set()
while q:
    cur = heapq.heappop(q)

    x = (cur[1], cur[2])
    if (cur[1], cur[2]) in visited:
        continue
    else:
        visited.add((cur[1], cur[2]))

    if (cur[1], cur[2]) == (SIZE - 1, SIZE - 1):
        print(cur[0])
        break

    adj = getAdjacents((cur[1], cur[2]))
    for i in adj:
        heapq.heappush(q, (cur[0] + 1, i[0], i[1]))



def printGrid(v):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (i, j) in v:
                print("O", end="")
            else:
                print(grid[i][j], end="")
        print()

for i in range(1024, len(data)):
    grid[data[i][0]][data[i][1]] = "#"
    #printGrid()
    #print()
    visited = set()
    good = False
    if i == len(data) - 1:
        print()
    q = [(0, 0, 0)]
    heapq.heapify(q)
    print(i)
    while q:
        cur = heapq.heappop(q)

        x = (cur[1], cur[2])
        if (cur[1], cur[2]) in visited:
            continue
        else:
            visited.add((cur[1], cur[2]))

        if (cur[1], cur[2]) == (SIZE - 1, SIZE - 1):
            good = True
            break

        adj = getAdjacents((cur[1], cur[2]))
        for j in adj:
            heapq.heappush(q, (cur[0] + 1, j[0], j[1]))
    if not good:
        print(data[i][1], end=",")
        print(data[i][0])
        break

'''
for i in range(len(grid)):
    for j in range(len(grid)):
        if (i, j) in visited:
            print("O", end="")
        else:
            print(grid[i][j], end="")
    print()
'''