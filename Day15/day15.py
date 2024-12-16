f = open("Day15/input.txt")
data = f.readlines()
data = [i.replace("\n", "") for i in data]
moves = ''.join(data)

f = open("Day15/grid.txt")
grid = f.readlines()
grid = [i.replace("\n", "") for i in grid]
grid = [[i for i in j] for j in grid]


startPos = ()
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == "@":
            startPos = (i, j)
            grid[i][j] = "."
            break

def printGrid(pos):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == pos:
                print("@", end="")
            else:
                print(grid[i][j], end="")
        print()

def addTuple(a, b):
    return (a[0] + b[0], a[1] + b[1])

moveDirs = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
def move(d, pos):
    newPos = addTuple(pos, moveDirs[d])
    boxes = 0
    while True:
        temp = grid[newPos[0]][newPos[1]]
        if temp == "O":
            boxes += 1
            newPos = addTuple(newPos, moveDirs[d])
        elif temp == ".":
            break
        else:
            return pos

    toMove = addTuple(pos, moveDirs[d])
    if boxes == 0:
        return toMove
    
    grid[toMove[0]][toMove[1]] = "."
    grid[pos[0] + (boxes + 1) * moveDirs[d][0]][pos[1] + (boxes + 1) * moveDirs[d][1]] = "O"
    return toMove

pos = startPos
for i in moves:
    #printGrid(pos)
    #print()
    #print()
    pos = move(i, pos)

count = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        print(grid[i][j], end="")
        if grid[i][j] == "O":
            count += 100 * i + j
    print()
print(count)

f = open("Day15/grid.txt")
grid = f.readlines()
grid = [i.replace("\n", "") for i in grid]
grid = [i.replace("@", ".") for i in grid]
grid = [[i for i in j] for j in grid]


newGrid = []
for i in grid:
    temp = []
    for j in i:
        if j == "#":
            temp.append("#")
            temp.append("#")
        if j == ".":
            temp.append(".")
            temp.append(".")
        if j == "O" or j == "@":
            temp.append("[")
            temp.append("]")
    newGrid.append([k for k in temp])

grid = [i for i in newGrid]

startPos = (startPos[0], startPos[1] * 2)
#printGrid(startPos)

def maxPush(pos, d):
    newPos = addTuple(pos, moveDirs[d])
    x = grid[newPos[0]][newPos[1]]
    if x == "#":
        return 0
    elif x == ".":
        return 1
    elif x == "[":
        return min(maxPush(newPos, d), maxPush((newPos[0], newPos[1] + 1), d))
    elif x == "]":
        return min(maxPush(newPos, d), maxPush((newPos[0], newPos[1] - 1), d))

def move2(d, pos):
    newPos = addTuple(pos, moveDirs[d])

    if d in ("^", "v"):
        pushes = maxPush(pos, d)
        if grid[newPos[0]][newPos[1]] == ".":
            grid[newPos[0]][newPos[1]] = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = "."
            return newPos
        elif pushes == 0 or grid[newPos[0]][newPos[1]] == "#":
            return pos
        else:
            thing = grid[newPos[0]][newPos[1]]
            if thing == "[":
                move2(d, newPos)
                move2(d, (newPos[0], newPos[1] + 1))
            elif thing == "]": 
                move2(d, newPos)
                move2(d, (newPos[0], newPos[1] - 1))
            grid[newPos[0]][newPos[1]] = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = "."
            return newPos
    else:
        boxes = 0
        while True:
            temp = grid[newPos[0]][newPos[1]]
            if temp in ("[", "]"):
                boxes += 1
                newPos = addTuple(newPos, moveDirs[d])
            elif temp == ".":
                break
            else:
                return pos

        toMove = addTuple(pos, moveDirs[d])
        if boxes == 0:
            return toMove
        
        for i in range(boxes + 1, 0, -1):
            grid[pos[0]][pos[1] + i * moveDirs[d][1]] = grid[pos[0]][pos[1] + (i - 1) * moveDirs[d][1]]
            grid[pos[0]][pos[1] + (i - 1) * moveDirs[d][1]] = "."

        return toMove
    

pos = startPos
x = 0
for i in moves:
    x += 1
    #printGrid(pos)
    #print()
    #print()
    pos = move2(i, pos)

count = 0
print()
print()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end="")
        if grid[i][j] == "[":
            count += 100 * i + j
    print()
print(count)