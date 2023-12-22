from queue import Queue

with open("day21_input.txt") as f:
    a = [list(i.replace("\n", "")) for i in f.readlines()]


def in_bounds(point: tuple[int, int], board: list[list[str]]) -> bool:
    x, y = point
    if (x > len(board) - 1) or (x < 0) or (y > len(board[0]) - 1) or (y < 0):
        return False
    return True


start_pos = (0, 0)
BLOCKS = set()
for row_num, row in enumerate(a):
    for col_num, val in enumerate(row):
        if val == "S":
            start_pos = (row_num, col_num)
            a[row_num][col_num] = "0"
        if val == "#":
            BLOCKS.add((row_num, col_num))


def walk_board(board, start_pos, max_steps):
    out = 0
    visited = set()
    q = Queue()
    q.put((start_pos, 0))
    while not q.empty():
        pos, steps = q.get()

        if pos in visited:
            continue
        visited.add(pos)

        if steps % 2 == max_steps % 2:
            out += 1

        if steps >= max_steps:
            continue

        for heading in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = tuple([x + y for x, y in zip(pos, heading)])
            adj_pos = (new_pos[0] % len(board), new_pos[1] % len(board[0]))
            if adj_pos in BLOCKS:
                continue
            q.put((new_pos, steps + 1))

    return out


print(f"Part 1: {walk_board(a, start_pos, 64)}")

# Part 2
steps_to_take = 26501365

n = steps_to_take // len(a[0])

a, b, c = [walk_board(a, start_pos, i * len(a[0]) + start_pos[1]) for i in range(0, 3)]
quadratic_magic = a + n * (b - a + (n - 1) * (c - 2 * b + a) // 2)
print(f"Part 2: {quadratic_magic}")
