grid = []
f = open("Day11/input.txt")
for line in f:
    line = line.replace("\n", "")
    line = line.split(" ")
    grid.append([int(i) for i in line])

stones = [i for i in grid[0]]


def blink(stones):
    new = []
    for s in stones:
        if s == 0:
            new.append(1)
        elif len(str(s)) % 2 == 0:
            new.append(int(str(s)[:len(str(s)) // 2]))
            new.append(int(str(s)[len(str(s)) // 2:]))
        else:
            new.append(s * 2024)
    stones = [i for i in new]
    return stones


for i in range(25):
    stones = blink(stones)

print(len(stones))

stones = [i for i in grid[0]]

dp = {}

def blinkDP(s, blinksLeft):
    global dp
    if (s, blinksLeft) in dp:
        return dp[(s, blinksLeft)]
    if blinksLeft == 0:
        return 1
    
    count = 0
    if s == 0:
        count = blinkDP(1, blinksLeft - 1)
    elif len(str(s)) % 2 == 0:
        count += blinkDP(int(str(s)[:len(str(s)) // 2]), blinksLeft - 1)
        count += blinkDP(int(str(s)[len(str(s)) // 2:]), blinksLeft - 1)
    else:
        count += blinkDP(s * 2024, blinksLeft - 1)
    dp[(s, blinksLeft)] = count
    return count

count = 0
for s in stones:
    count += blinkDP(s, 75)
print(len(dp))
print(count)