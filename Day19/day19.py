f = open("Day19/input.txt")
data = f.readlines()
data = [i.replace("\n", "") for i in data]

towels = data[0]
towels = towels.split(", ")

data = data[2:]


dp = {}

def possible(t: str):
    if t in dp:
        return dp[t]
    if len(t) == 0:
        return 1
    
    count = 0
    for i in towels:
        if t.startswith(i):
            count += possible(t[len(i):])

    dp[t] = count
    return count


count = 0
for i in data:
    count += 1 if possible(i) != 0 else 0
print(count)

count = 0
for i in data:
    count += possible(i)
print(count)