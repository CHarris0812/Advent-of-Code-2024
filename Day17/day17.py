f = open("Day17/input.txt")
data = f.readlines()
data = [i.replace("\n", "") for i in data]

registers = [0, 0, 0]
for i in range(3):
    registers[i] = int(data[i].split(": ")[1])

program = data[4].split(": ")[1].split(",")
program = [int(i) for i in program]

vals = {0:0, 1:1, 2:2, 3:3, 4:registers[0], 5:registers[1], 6:registers[2]}

pointer = 0
result = ""
while pointer < len(program):
    operator = program[pointer]
    operand = program[pointer + 1]
    #print(operator, operand)
    pointer += 2

    if operator == 0:
        vals[4] = vals[4] // (2 ** vals[operand])
    elif operator == 1:
        vals[5] = vals[5] ^ operand
    elif operator == 2:
        vals[5] = vals[operand] % 8
    elif operator == 3:
        if vals[4] != 0:
            pointer = operand
    elif operator == 4:
        vals[5] = vals[5] ^ vals[6]
    elif operator == 5:
        result += str(vals[operand] % 8)
        result += ","
    elif operator == 6:
        vals[5] = vals[4] // (2 ** vals[operand])
    elif operator == 7:
        vals[6] = vals[4] // (2 ** vals[operand])

print(result[:-1])
goal = [str(i) for i in program]
goal = ",".join(goal)
goal += ","

'''
dp = {}
#(A // 8, A % 8)

count = 0
for i in range(2 ** 7): #A // (2 ** B)
    for j in range(2 ** 3): #A % 8      B
        pointer = 0
        result = ""
        vals = {0:0, 1:1, 2:2, 3:3, 4:i * 8 + j, 5:registers[1], 6:registers[2]}
        
        while pointer < len(program):
            operator = program[pointer]
            operand = program[pointer + 1]
            pointer += 2

            if operator == 0:
                vals[4] = vals[4] // (2 ** vals[operand])
            elif operator == 1:
                vals[5] = vals[5] ^ operand
            elif operator == 2:
                vals[5] = vals[operand] % 8
            elif operator == 3:
                if vals[4] != 0:
                    pointer = operand
            elif operator == 4:
                vals[5] = vals[5] ^ vals[6]
            elif operator == 5:
                dp[(i, j)] = vals[operand] % 8
                break
            elif operator == 6:
                vals[5] = vals[4] // (2 ** vals[operand])
            elif operator == 7:
                vals[6] = vals[4] // (2 ** vals[operand])




def minValid(pointer, x):
    #X represents A // 8
    if pointer == len(program):
        return 0
    target = program[pointer]
    for i in dp:
        if i[0] == x:
            if dp[i] == target:
                val = minValid(pointer + 1, i[1])
                if val != -1:
                    return 8 * x + val
    return -1


for i in dp:
    if dp[i] == program[0]:
        val = minValid(1, i[1])
        if val != -1:
            print((i[0] * 8 + val) // 8)
'''

dp = {}
def solve(a):
    if a in dp:
        return dp[a]
    
    vals = {0:0, 1:1, 2:2, 3:3, 4:a, 5:registers[1], 6:registers[2]}
    
    pointer = 0
    while pointer < len(program):
        operator = program[pointer]
        operand = program[pointer + 1]
        pointer += 2

        if operator == 0:
            vals[4] = vals[4] // (2 ** vals[operand])
        elif operator == 1:
            vals[5] = vals[5] ^ operand
        elif operator == 2:
            vals[5] = vals[operand] % 8
        elif operator == 3:
            if vals[4] != 0:
                pointer = operand
        elif operator == 4:
            vals[5] = vals[5] ^ vals[6]
        elif operator == 5: 
            return vals[operand] % 8
        elif operator == 6:
            vals[5] = vals[4] // (2 ** vals[operand])
        elif operator == 7:
            vals[6] = vals[4] // (2 ** vals[operand])

'''
dp = {}
count = 0
for a in range(2 ** 10):
    pointer = 0
    result = ""
    vals = {0:0, 1:1, 2:2, 3:3, 4:a, 5:registers[1], 6:registers[2]}
    
    while pointer < len(program):
        operator = program[pointer]
        operand = program[pointer + 1]
        pointer += 2

        if operator == 0:
            vals[4] = vals[4] // (2 ** vals[operand])
        elif operator == 1:
            vals[5] = vals[5] ^ operand
        elif operator == 2:
            vals[5] = vals[operand] % 8
        elif operator == 3:
            if vals[4] != 0:
                pointer = operand
        elif operator == 4:
            vals[5] = vals[5] ^ vals[6]
        elif operator == 5:
            dp[a] = vals[operand] % 8
            break
        elif operator == 6:
            vals[5] = vals[4] // (2 ** vals[operand])
        elif operator == 7:
            vals[6] = vals[4] // (2 ** vals[operand])

print()
'''


goal = program[::-1]
def findA(a, depth):
    if depth == len(goal): return a

    for i in range(8):
        x = solve(a * 8 + i)
        if int(str(x)[0]) == goal[depth]:
            r = findA(a * 8 + i, depth + 1)
            if r != 0:
                return r
    return 0

print(findA(0, 0))

'''
16 prints
Therefore A = 0 after 16 run throughs


2,4,        B = A % 8
1,3,        B = B ^ 3
7,5,        C = A / (2 ** B)
1,5,        B = B ^ 5
0,3,        A = A / (2 ** 3)
4,3,        B = B ^ C
5,5,        Output += B % 8
3,0         Pointer = 0 if A != 0


8 ^ 14 < A < 8 ^ 15


1st run through
Output: 2

B = A % 8
B = B ^ 3
C = A / (2 ** B)
B = B ^ 5
B = B ^ C
B % 8 = 2

(A, 1, 0)
(A, 6, 0)
(A, 1, 0)


B = B ^ 3 ^ 5
B = !B[0] !B[1] B[2]

If B == 1:
    2 == 1 ^ C
    C == 8 * X + 3


Dynamic programming
(A % 8, A // (2 ** (A % 8)) % 8)
'''