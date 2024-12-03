import re

inp = ""
f = open("Day3/input.txt")
for line in f:
    line = line.replace("\n", "")
    inp += line

regex = r"mul\(\d+,\d+\)"
ops = re.findall(regex, inp)
#print(ops)

stuff = list(map(lambda x: x[4:-1], ops))
#print(stuff)

count = 0
for i in stuff:
    left, right = map(int, i.split(","))
    count += left * right
print(count)

count = 0
do = True
for i in range(len(inp)):
    try:
        if inp[i:i+4] == "do()":
            do = True
            i += 3
        elif inp[i:i+7] == "don't()":
            do = False
            i += 6
        elif inp[i:i+4] == "mul(":
            end = inp.find(")", i)
            if end:
                thing = inp[i:end + 1]
                if re.match(regex, thing):
                    thing = thing[4:-1]
                    left, right = map(int, thing.split(","))
                    if do: count += left * right
                i = end - 1
    except:
        pass
    i += 1
print(count)