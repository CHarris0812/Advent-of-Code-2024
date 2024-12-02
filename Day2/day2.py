def isValid(report):
    increasing = False
    if report[1] > report[0]: increasing = True
    for i in range(1, len(report)):
        if increasing and report[i] <= report[i - 1]: return False
        if not increasing and report[i] >= report[i - 1]: return False
        dif = abs(report[i] - report[i - 1])
        if dif < 1 or dif > 3: return False
    return True

reports = []
f = open("Day2/input.txt")
for line in f:
    line = line[:-1]
    temp = line.split(" ")
    temp = [int(i) for i in temp]
    reports.append(temp)

count = 0
for r in reports:
    if isValid(r):
        count += 1
print(count)

count = 0
for r in reports:
    trueForAny = isValid(r)
    for i in range(len(r)):
        if isValid(r[:i] + r[i+1:]): trueForAny = True
    if trueForAny: count += 1
print(count)