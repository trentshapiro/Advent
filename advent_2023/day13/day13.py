with open("day13_input.txt") as f:
    a = [i.split("\n") for i in f.read().split("\n\n")]


def find_reflection(pattern: list[str], leniency: int) -> int:
    prev_lines = [pattern[0]]
    for idx, line in enumerate(pattern[1:]):
        cursor = idx + 1
        if sum(1 for a, b in zip(line, prev_lines[-1]) if a != b) <= leniency:
            line_count = min(len(prev_lines), len(pattern[cursor:]))
            rest = pattern[cursor : cursor + line_count]
            prev = prev_lines[::-1][:line_count]

            if sum(1 for x, y in zip(rest, prev) for i, j in zip(x, y) if i != j) == leniency:
                return cursor

        prev_lines.append(line)
    return -1


idx = [0, 0]
for pattern in a:
    for i in range(0, 2):
        index = find_reflection(pattern, i)
        if index < 0:
            rotated = ["".join(list(reversed(col))) for col in zip(*pattern)]
            index = find_reflection(rotated, i)
            idx[i] += index
        else:
            idx[i] += index * 100

print(f"Part 1: {idx[0]}")
print(f"Part 2: {idx[1]}")
