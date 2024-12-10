inp = ""
f = open("Day09/input.txt")
for line in f:
    line = line.replace("\n", "")
    inp = line

block = []
space = False
count = 0
for i in inp:
    if space:
        for j in range(int(i)):
            block.append(".")
    else:
        for j in range(int(i)):
            block.append(count)
        count += 1
    space = not space

p1 = 0
p2 = len(block) - 1
while p1 < p2:
    if block[p1] != ".":
        p1 += 1
    elif block[p2] == ".":
        p2 -= 1
    else:
        block[p1] = block[p2]
        block[p2] = 0
        p1 += 1
        p2 -= 1

count = 0
for i in range(len(block)):
    if block[i] != ".":
        count += i * int(block[i])
print(count)

block = []
space = False
count = 0
for i in inp:
    if i != "0":
        if space:
            block.append((".", int(i)))
        else:
            block.append((count, int(i)))
            count += 1
    space = not space

i = len(block) - 1
while i >= 0:
    if block[i][0] != ".":
        l = block[i][1]
        for j in range(i):
            if block[j][0] == "." and block[j][1] >= l:
                if block[j][1] == l:
                    block[j] = block[i]
                    block[i] = (".", l)
                else:
                    x = block[j][1]
                    block[j] = block[i]
                    temp = "." * (x - l)
                    block.insert(j + 1, (".", x - l))
                    block[i + 1] = (".", l)
                    i += 1
                break
    i -= 1



b = []
for i in block:
    for j in range(i[1]):
        b.append(i[0])

count = 0
for i in range(len(b)):
    if b[i] != ".":
        count += i * b[i]
print(count)