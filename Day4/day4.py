
grid = []
f = open("Day4/input.txt")
for line in f:
    line = line.replace("\n", "")
    grid.append(line)



def countXmas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Down-Right
        (-1, -1),# Up-Left
        (1, -1), # Down-Left
        (-1, 1)  # Up-Right
    ]
    
    def isValid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                x, y = r, c
                match = True
                for char in "XMAS":
                    if not isValid(x, y) or grid[x][y] != char:
                        match = False
                        break
                    x += dx
                    y += dy
                if match:
                    count += 1
    
    return count

def countXmas2(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    directions = [
        (1, 1),  # Down-Right
        (-1, -1),# Up-Left
        (1, -1), # Down-Left
        (-1, 1)  # Up-Right
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A":
                numGood = 0
                for dx, dy in directions:
                    x, y = r - dx, c - dy
                    match = True
                    for char in "MAS":
                        if not is_valid(x, y) or grid[x][y] != char:
                            match = False
                            break
                        x += dx
                        y += dy
                    if match: numGood += 1
                if numGood == 2:
                    count += 1

    return count


print(countXmas(grid))
print(countXmas2(grid))