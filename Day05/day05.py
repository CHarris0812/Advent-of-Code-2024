updates = []
f = open("Day5/updates.txt")
for line in f:
    line = line.replace("\n", "")
    updates.append([int(i) for i in line.split(",")])

rules = []
f = open("Day5/rules.txt")
for line in f:
    line = line.replace("\n", "")
    line = line.split("|")
    rules.append((int(line[0]), int(line[1])))

count = 0
for u in updates:
    seen = []
    good = True
    for i in u:
        for s in seen:
            if (i, s) in rules:
                good = False
        seen.append(i)
    if good: 
        count += u[len(u) // 2]
print(count)

def isValid(u):
    seen = []
    for i in u:
        for s in seen:
            if (i, s) in rules:
                return u.index(i)
        seen.append(i)
    return -1


prev = count
count = 0
for u in updates:
    ind = isValid(u)
    while ind != -1:
        temp = u[ind]
        u[ind] = u[ind - 1]
        u[ind - 1] = temp
        ind = isValid(u)

    count += u[len(u) // 2]

print(count - prev)