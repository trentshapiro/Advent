import re

with open("day02_input.txt") as f:
    a = f.readlines()
    a = [i.replace('\n','') for i in a]

total = 0
power = 0

for i, line in enumerate(a):
    max_r = max([int(i) for i in re.findall("[0-9]{1,5}(?= red)",line)])
    max_g = max([int(i) for i in re.findall("[0-9]{1,5}(?= green)",line)])
    max_b = max([int(i) for i in re.findall("[0-9]{1,5}(?= blue)",line)])

    if (max_r <= 12) and (max_g <= 13) and (max_b <= 14):
        total += (i+1)

    power = power + (max_r * max_b * max_g)

print(total)
print(power)
