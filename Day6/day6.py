grid = []
f = open("Day6/input.txt")
i = 0
guardRow = 0
guardCol = 0
guardDir = "U"
for line in f:
    line = line.replace("\n", "")
    if "^" in line:
        guardRow = i
        guardCol = line.index("^")
        line = line.replace("^", ".")
    i += 1
    grid.append(line)

guardPos = (guardRow, guardCol)
dirs = {"U":(-1, 0), "D":(1, 0), "R":(0, 1), "L":(0, -1)}
dirOrder = ["U", "R", "D", "L"]

def inBound(r, c):
    if r < 0 or r >= len(grid): return False
    if c < 0 or c >= len(grid[0]): return False
    return True

while True:
    grid[guardPos[0]] = grid[guardPos[0]][:guardPos[1]] + "X" + grid[guardPos[0]][guardPos[1] + 1:]
    r = guardPos[0] + dirs[guardDir][0]
    c = guardPos[1] + dirs[guardDir][1]
    if not inBound(r, c): break

    if grid[r][c] == "#":
        guardDir = dirOrder[(dirOrder.index(guardDir) + 1) % 4]
    else:
        guardPos = (r, c)

print(sum([i.count("X") for i in grid]))

def reachesExit(guardPos, guardDir):
    visited = set()
    while True:
        r = guardPos[0] + dirs[guardDir][0]
        c = guardPos[1] + dirs[guardDir][1]
        if not inBound(r, c): return True

        if grid[r][c] == "#":
            guardDir = dirOrder[(dirOrder.index(guardDir) + 1) % 4]
            
            temp = (guardDir, guardPos[0], guardPos[1])
            if temp in visited: 
                return False
            else:
                visited.add(temp)
        else:
            guardPos = (r, c)

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        guardPos = (guardRow, guardCol)
        guardDir = "U"
        if i == guardRow and j == guardCol:
            continue
        if grid[i][j] == "#" or grid[i][j] == ".":
            continue
        grid[i] = grid[i][:j] + "#" + grid[i][j+1:]
        if not reachesExit(guardPos, guardDir): count += 1
        grid[i] = grid[i][:j] + "X" + grid[i][j+1:]
print(count)