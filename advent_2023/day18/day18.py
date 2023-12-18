import numpy as np
import math

with open("day18_input.txt") as f:
    a = [i.replace("\n", "").split(" ") for i in f.readlines()]

MAP = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}
HEX_MAP = {"0": "R", "1": "D", "2": "L", "3": "U"}


def calc_area(vertices):
    perimeter = 1
    for start, end in vertices:
        perimeter += int(math.dist(start, end))

    points = [i[0] for i in vertices]

    adj_x = -min([i[0] for i in points])
    adj_y = -min([i[1] for i in points])
    points = np.array([(i + adj_x, j + adj_y) for i, j in points])
    points = points.reshape(-1, 2)
    area = np.abs(
        np.dot(points[:, 0], np.roll(points[:, 1], 1))
        - np.dot(points[:, 1], np.roll(points[:, 0], 1))
    )

    return math.ceil((area + perimeter) / 2)


start, color_start = [0, 0], [0, 0]
walls = []
color_walls = []
for i in a:
    heading, run, color = i
    run = int(run)
    color = color[2:-1]
    color_run = int(color[0:-1], 16)
    color_heading = HEX_MAP[color[-1]]

    # P1
    movement = [i * run for i in MAP[heading]]
    end = [x + y for x, y in zip(start, movement)]
    walls.append([start, end])
    start = end

    # P2
    movement = [i * color_run for i in MAP[color_heading]]
    color_end = [x + y for x, y in zip(color_start, movement)]
    color_walls.append([color_start, color_end])
    color_start = color_end

print(f"Part 1: {calc_area(walls)}")
print(f"Part 2: {calc_area(color_walls)}")
