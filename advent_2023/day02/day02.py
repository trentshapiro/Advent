import re

with open("day02_input.txt") as f:
    a = f.readlines()
    a = [i.replace('\n','') for i in a]

# Part 1
total = 0
for line in a:
    max_r, max_g, max_b = 12, 13, 14
    game_num = int(line.split(":")[0].split(" ")[-1])

    #check numbers 
    games = line.split(":")[-1]
    matches = [m.span() for m in re.finditer(pattern="[0-9]{2,99}", string=games)]
    if len(matches) == 0:
        total += game_num
        continue
    else:
        impossible = False
        for res in [games[s:e+3] for s,e in matches]:
            game_count = int(res.split(" ")[0])
            game_col = res.split(" ")[1]
            if game_col == "re" and game_count > max_r:
                impossible = True
                break
            if game_col == "gr" and game_count > max_g:
                impossible = True
                break
            if game_col == "bl" and game_count > max_b:
                impossible = True
                break
        if not impossible:
            total += game_num

print(total)

# Part 2
power = 0
for line in a:
    min_red = max([int(i) for i in re.findall("[0-9]{1,5}(?= red)",line)])
    min_blue = max([int(i) for i in re.findall("[0-9]{1,5}(?= blue)",line)])
    min_green = max([int(i) for i in re.findall("[0-9]{1,5}(?= green)",line)])

    power = power + (min_red * min_blue * min_green)

print(power)
