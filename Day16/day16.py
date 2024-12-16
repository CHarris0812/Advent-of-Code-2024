f = open("Day16/input.txt")
data = f.readlines()
data = [i.replace("\n", "") for i in data]

grid = []
for i in data:
    grid.append([j for j in i])

import heapq
q = [(1000, (len(grid) - 2, 1), 'N'), (0, (len(grid) - 2, 1), 'E')]
heapq.heapify(q)
dirs = {"N":(-1, 0), "S":(1, 0), "E":(0, 1), "W":(0, -1)}

def add(a, b):
    temp = [a[i] + b[i] for i in range(len(a))]
    return tuple(temp)

def valid(pos):
    if 0 <= pos[0] and 0 <= pos[1] and pos[0] < len(grid) and pos[1] < len(grid[0]):
        return True
    return False


visited = set()
while True:
    cur = heapq.heappop(q)
    pos = cur[1]
    x = (pos, cur[-1])
    if x in visited:
        continue
    else:
        visited.add(x)
    if grid[pos[0]][pos[1]] == "E":
        print(cur[0])
        break
    elif grid[pos[0]][pos[1]] != "#":
        if valid(add(pos, dirs[cur[-1]])):
            heapq.heappush(q, (cur[0] + 1, add(pos, dirs[cur[-1]]), cur[-1]))
        for i in "NESW":
            heapq.heappush(q, (cur[0] + 1000, pos, i))



a = ((len(grid) - 2, 1), "N")
x = (1000, (len(grid) - 2, 1), 'N', tuple([a]))

b = ((len(grid) - 2, 1), "E")
y = (0, (len(grid) - 2, 1), 'E', tuple([b]))

q = [x, y]
heapq.heapify(q)

minCost = 1000000000
visited = {}
paths = []
potentials = {}
while True:
    cur = heapq.heappop(q)

    if cur[0] > minCost: break

    pos = cur[1]
    x = (pos, cur[-2])

    if x in visited:
        if visited[x] < cur[0]:
            continue
        elif visited[x] == cur[0]:
            if x in potentials:
                potentials[x].append(cur[-1])
            else:
                potentials[x] = [cur[-1]]
            continue

    else:
        visited[x] = cur[0]

    if grid[pos[0]][pos[1]] == "E":
        minCost = cur[0]
        paths.append(cur[-1])
        continue
    elif grid[pos[0]][pos[1]] != "#":
        if valid(add(pos, dirs[cur[-2]])):
            temp = [i for i in cur[-1]]
            temp.append((add(pos, dirs[cur[-2]]), cur[-2]))
            heapq.heappush(q, (cur[0] + 1, add(pos, dirs[cur[-2]]), cur[-2], tuple(temp)))
        for i in "NESW":
            temp = [i for i in cur[-1]]
            temp.append((pos, i))
            heapq.heappush(q, (cur[0] + 1000, pos, i, tuple(temp)))

count = 0
v2 = set()
for p in paths:
    for i in p:
        if i[0] not in v2:
            v2.add(i[0])
        if i in potentials:
            for x in potentials[i]:
                for j in x:
                    if j[0] not in v2:
                        v2.add(j[0])
                    if j in potentials:
                        for a in potentials[j]:
                            for b in a:
                                if b[0] not in v2:
                                    v2.add(b[0])
print(len(v2))


'''
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) in v2:
            print("O", end="")
            count += 1
        else:
            print(grid[i][j], end="")
    print()
print(count)
'''