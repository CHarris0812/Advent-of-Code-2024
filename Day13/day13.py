machines = []
f = open("Day13/input.txt")
stuff = f.readlines()

while len(stuff) > 0:
    x = stuff.pop(0)
    y = stuff.pop(0)
    z = stuff.pop(0)
    try:
        t = stuff.pop(0)
    except:
        print()

    a = x.split(": ")[1]
    a = a.split(", ")
    a = [int(i[2:]) for i in a]
    a = tuple(a)

    b = y.split(": ")[1]
    b = b.split(", ")
    b = [int(i[2:]) for i in b]
    b = tuple(b)

    c = z.split(": ")[1]
    c = c.split(", ")
    c = [int(i[2:]) for i in c]
    c = tuple(c)

    machines.append([a, b, c])



def getCost(m):
    a = m[0]
    b = m[1]
    g = m[2]
    g = (g[0] + 10000000000000, g[1] + 10000000000000)

    '''
    d = {}
    m = 100000000000000000
    frontier = [(0, 0, 0)]
    while frontier:
        cur = frontier.pop()
        if (cur[1], cur[2]) == g:
            m = min(m, cur[0])
        else:
            if cur[1] > g[0] or cur[2] > g[1]:
                continue
            else:
                if (cur[1], cur[2]) not in d or d[(cur[1], cur[2])] > cur[0]:
                    d[(cur[1], cur[2])] = cur[0]
                    frontier.append((cur[0] + 3, cur[1] + a[0], cur[2] + a[1]))
                    frontier.append((cur[0] + 1, cur[1] + b[0], cur[2] + b[1]))

    if m == 100000000000000000: return 0
    return m
    '''

    '''
    m = 100000000000000000
    for i in range(2 + g[0] // a[0]):
        for j in range(1000):
            if a[0] * i + b[0] * j == g[0] and a[1] * i + b[1] * j == g[1]:
                m = min(m, i * 3 + j)
    if m == 100000000000000000: return 0
    return m
    '''

    x = (g[0] * b[1] - g[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
    y = (g[1] * a[0] - g[0] * a[1]) / (a[0] * b[1] - a[1] * b[0])
    if int(x) == x and int(y) == y:
        return int(x * 3 + y)
    return 0



count = 0
for m in machines:
    count += getCost(m)
print(count)