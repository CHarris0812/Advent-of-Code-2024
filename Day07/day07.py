grid = []
f = open("Day07/input.txt")
for line in f:
    line = line.replace("\n", "")
    temp = line.split(": ")
    temp[1] = temp[1].split(" ")
    temp[1] = [int(i) for i in temp[1]]
    grid.append((int(temp[0]), temp[1]))


total = 0
for i in grid:
    goal = i[0]
    nums = i[1]
    for j in range(2 ** (len(nums) - 1)):
        binNum = str(bin(j))[2:]
        binNum = "0" * ((len(nums) - 1) - len(binNum)) + binNum
        binNum = binNum.replace("0", "+")
        binNum = binNum.replace("1", "*")

        cur = nums[0]
        for i in range(len(nums) - 1):
            if binNum[i] == "*":
                cur *= nums[i+1]
            else:
                cur += nums[i+1]
        if cur == goal:
            total += goal
            break
print(total)

def convertBase3(n):
    base3 = []
    while n:
        base3.append(str(n % 3))
        n //= 3
    return "".join(reversed(base3))


total = 0
for i in grid:
    goal = i[0]
    nums = i[1]
    for j in range(3 ** (len(nums) - 1)):
        binNum = convertBase3(j)
        binNum = "0" * ((len(nums) - 1) - len(binNum)) + binNum
        binNum = binNum.replace("0", "+")
        binNum = binNum.replace("1", "*")

        cur = nums[0]
        for i in range(len(nums) - 1):
            if binNum[i] == "*":
                cur *= nums[i+1]
            elif binNum[i] == "+":
                cur += nums[i+1]
            else:
                cur = int(str(cur) + str(nums[i + 1]))
        if cur == goal:
            total += goal
            break
print(total)