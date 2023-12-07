import re

with open("day02_input.txt") as f:
    a = f.readlines()
    a = [i.replace('\n','') for i in a]

total, power = 0, 0
for i, line in enumerate(a):
    c = [max([int(i) for i in re.findall(f"[0-9]{{1,5}}(?= {i})",line)]) for i in ["red","green","blue"]]
    total += (i+1) if (c[0] <= 12) and (c[1] <= 13) and (c[2] <= 14) else 0
    power += (c[0]*c[1]*c[2])

print(total)
print(power)
