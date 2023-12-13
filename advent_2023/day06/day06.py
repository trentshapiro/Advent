import re


with open("day06_input.txt") as f:
    a = f.readlines()
    a = [i.replace("\n", "") for i in a]

ts = [int(i) for i in re.findall("\d+", a[0])]
ds = [int(i) for i in re.findall("\d+", a[1])]

wins = 1
for i in range(0, len(ts)):
    this_win_count = 0
    for j in range(0, ts[i]):
        dist = j * (ts[i] - j)
        if dist > ds[i]:
            this_win_count += 1

    wins = wins * this_win_count

print(wins)

ts = int("".join([str(i) for i in ts]))
ds = int("".join([str(i) for i in ds]))

this_win_count = 0
for j in range(0, ts):
    dist = j * (ts - j)
    if dist > ds:
        this_win_count += 1

print(this_win_count)
