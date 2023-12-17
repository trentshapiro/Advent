from queue import PriorityQueue
import time

st = time.time()

with open("day17_input.txt") as f:
    WEIGHTS = [[int(j) for j in i.replace("\n", "")] for i in f.readlines()]


def in_bounds(point: tuple[int, int], mat: list[list[int]]) -> bool:
    x, y = point
    if (x > len(mat) - 1) or (x < 0) or (y > len(mat[0]) - 1) or (y < 0):
        return False
    return True


def traverse_weights(weights, min_run, max_run):
    checked_nodes = set()

    q = PriorityQueue()
    q.put((0, (0, 0), (0, 1), 1))
    q.put((0, (0, 0), (1, 0), 1))

    while q != []:
        heat, point, heading, run = q.get()

        # check history
        checked = (point, heading, run)
        if checked in checked_nodes:
            continue
        checked_nodes.add(checked)

        new_point = tuple([x + y for x, y in zip(point, heading)])

        if not in_bounds(new_point, weights):
            continue

        new_heat = heat + weights[new_point[0]][new_point[1]]

        # finished
        if new_point == (len(weights) - 1, len(weights[0]) - 1):
            return new_heat

        # base case
        for new_heading in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            # dont go backward
            if new_heading == tuple([i * -1 for i in heading]):
                continue

            if run < min_run and heading != new_heading:
                continue

            new_run = run + 1 if new_heading == heading else 1

            if new_run > max_run:
                continue

            q.put((new_heat, new_point, new_heading, new_run))


print(f"Part 1: {traverse_weights(WEIGHTS, 0, 3)}")
print(time.time() - st)
print(f"Part 2: {traverse_weights(WEIGHTS, 4, 10)}")
print(time.time() - st)
