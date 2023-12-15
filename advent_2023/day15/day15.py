from functools import reduce

with open("day15_input.txt") as f:
    a = f.readlines()
    a = [list(j) for i in a for j in i.replace("\n", "").split(",")]


def hash_scheme(a, b):
    return ((a + b) * 17) % 256


sum_hash = 0
boxes = {}
for line in a:
    sum_hash += reduce(hash_scheme, [ord(i) for i in line], 0)

    label, foc_len = "".join(line).replace("-", "=0").split("=")
    box_num = reduce(hash_scheme, [ord(i) for i in list(label)], 0)

    box = [] if box_num not in boxes.keys() else boxes[box_num]

    if label in [i for i, _ in box]:
        if int(foc_len) == 0:
            box = [i for i in box if i[0] != label]
        else:
            box = [(i, j) if i != label else (label, int(foc_len)) for i, j in box]
    elif int(foc_len) > 0:
        box.append((label, int(foc_len)))

    boxes[box_num] = box

total_power = sum(
    sum([(box_num + 1) * i[1] * (idx + 1) for idx, i in enumerate(values)])
    for box_num, values in boxes.items()
)

print(f"Part 1: {sum_hash}")
print(f"Part 2 : {total_power}")
