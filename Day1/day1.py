f = open("input.txt")
l1 = []
l2 = []
for line in f:
    line = line[:-1]
    temp = line.split(" ")
    l1.append(int(temp[0]))
    l2.append(int(temp[-1]))

l1.sort()
l2.sort()
total = 0
for i in range(len(l1)):
    total += abs(l1[i] - l2[i])
print(total)

counts = {}
for i in l2:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] += 1

similarity = 0
for i in l1:
    if i in counts:
        similarity += i * counts[i]
print(similarity)