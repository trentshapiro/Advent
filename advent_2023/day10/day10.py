import matplotlib.path as mpltPath


with open("day10_input.txt") as f:
    a = f.readlines()
    a = ["."+i.replace("\n","")+"." for i in a]

a = ["."*len(a[0]),*a,"."*len(a[0])]

for row_num, line in enumerate(a):
    if "S" in line:
        start = (row_num, line.index("S"))
        break

COMPASS = {
    "north":(-1, 0),
    "east" :( 0, 1),
    "south":( 1, 0),
    "west" :( 0,-1)
}

SOURCE_COMPASS = {
    "north":"south",
    "south":"north",
    "east" :"west",
    "west" :"east"
}

CHAR_MAP = {
    "|": ["north","south"],
    "-": ["east" ,"west"],
    "L": ["north","east"],
    "J": ["north","west"],
    "7": ["south","west"],
    "F": ["south","east"],
}

next_pos = [[start, "start"]]

def get_next_pos(pos,source_dir):
    current_char = a[pos[0]][pos[-1]]
    available_directions = [(i,j) for i,j in COMPASS.items()]

    if current_char != "S":
        direction = [i for i in CHAR_MAP[current_char] if i != source_dir][0]
        available_directions = [(i,j) for i,j in COMPASS.items() if i == direction]

    for direction, adj in available_directions:
        if direction == source_dir:
            continue

        new_x, new_y = pos[0]+adj[0], pos[1]+adj[1]
        check_char = a[new_x][new_y]

        if check_char == "S":
            return "END"

        if check_char not in CHAR_MAP.keys():
            continue

        if SOURCE_COMPASS[direction] in CHAR_MAP[check_char]:
            return[(new_x,new_y), SOURCE_COMPASS[direction]]
        else:
            continue

#Part 1
while next_pos[-1] != "END":
    next_pos.append(get_next_pos(*next_pos[-1]))

next_pos = next_pos[:-1]

#Part 2
polygon = [i for i,_ in next_pos]
path = mpltPath.Path(polygon)

a = [list(i) for i in a]
inside = 0
for row in range(0,len(a)):
    for col in range(0,len(a[0])):
        if (row,col) not in polygon:
            if path.contains_point((row,col)):
                a[row][col] = "+"
                inside+=1
            else:
                a[row][col] = "."

a = ["".join(i) for i in a]

for i in a:
    print(i)

print(f"Part 1: {(len(next_pos))//2}")
print(f"Part 2: {inside}")

