antennas = {}
f = open("Day08/input.txt")
r = 0
cols = 0
for line in f:
    line = line.replace("\n", "")
    line = [i for i in line]
    cols = len(line)
    for c in range(len(line)):
        if line[c] != "." and line[c] != "#":
            if line[c] in antennas:
                antennas[line[c]].append((r, c))
            else:
                antennas[line[c]] = [(r, c)]

    r += 1
rows = r

def valid(a, r, c):
    if a[0] - r >= 0 and a[0] - r < rows:
        if a[1] - c >= 0 and a[1] - c < cols:
            return True
    return False

locs = set()
for a in antennas:
    for i in range(len(antennas[a])):
        for j in range(len(antennas[a])):
            if i == j:
                continue
            a1 = antennas[a][i]
            a2 = antennas[a][j]
            rDist = a2[0] - a1[0]
            cDist = a2[1] - a1[1]
            if rDist % 3 == 0 and cDist % 3 == 0:
                locs.add((a1[0] - rDist // 3, a1[1] - cDist // 3))
            if valid(a1, rDist, cDist):
                locs.add((a1[0] - rDist, a1[1] - cDist))
print(len(locs))

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

locs = set()
for a in antennas:
    for i in range(len(antennas[a])):
        for j in range(len(antennas[a])):
            if i == j:
                continue
            a1 = antennas[a][i]
            a2 = antennas[a][j]
            rDist = a2[0] - a1[0]
            cDist = a2[1] - a1[1]

            g = gcd(rDist, cDist)
            rDist = rDist // g
            cDist = cDist // g

            k = 0
            while valid(a1, rDist * k, cDist * k):
                locs.add((a1[0] - rDist * k, a1[1] - cDist * k))
                k += 1
            
            k = 0
            while valid(a1, rDist * k, cDist * k):
                locs.add((a1[0] - rDist * k, a1[1] - cDist * k))
                k -= 1
print(len(locs))