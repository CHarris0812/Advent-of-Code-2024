f = open("Day14/input.txt")
data = f.readlines()
data = [i.replace("\n", "") for i in data]

robots = []
for line in data:
    line = line.replace("p=", "")
    line = line.replace("v=", "")
    line = line.replace(" ", ",")
    temp = line.split(",")
    robots.append(tuple([int(i) for i in temp]))

rows = 101
cols = 103
turns = 100

#rows = 11
#cols = 7


results = []
for r in robots:
    results.append(((r[0] + r[2] * turns) % rows, (r[1] + r[3] * turns) % cols))

quads = [0, 0, 0, 0]
for r in results:
    if r[0] < rows // 2:
        if r[1] < cols // 2:
            quads[0] += 1
        elif r[1] > cols // 2:
            quads[1] += 1
    elif r[0] > rows // 2:
        if r[1] < cols // 2:    
            quads[2] += 1
        elif r[1] > cols // 2:
            quads[3] += 1


print(quads[0] * quads[1] * quads[2] * quads[3])

robots = [(i[1], i[0], i[3], i[2]) for i in robots]
rows = 103
cols = 101

r = [list(i) for i in robots]
for i in range(10000000):
    '''
    temp = []
    points = set()
    for robot in r:
        temp.append(((robot[0] + robot[2]) % rows, (robot[1] + robot[3]) % cols, robot[2], robot[3]))
        points.add(((robot[0] + robot[2]) % rows, (robot[1] + robot[3]) % cols))
    r = [j for j in temp]
    '''
    '''
    rowCounts = [0 for i in range(cols)]
    for j in range(rows):
        for k in range(cols):
            if (j, k) in points:
                rowCounts[j] += 1

    if max(rowCounts) >= 20:
        print(i + 1)
        for j in range(rows):
            for k in range(cols):
                if (j, k) in points:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()
        print()
    '''

    points = set()
    for j in range(len(r)):
        r[j][0] = (r[j][0] + r[j][2]) % rows
        r[j][1] = (r[j][1] + r[j][3]) % cols
        points.add((r[j][0], r[j][1]))

    if len(points) == len(r):
        print(i + 1)