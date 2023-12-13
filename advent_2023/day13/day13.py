with open("day13_input.txt") as f:
    a = f.readlines()
    a = [i.replace("\n", "") for i in a]


def find_reflection(pattern: list[str], leniency: int, dir: str, excl: dict = None) -> int:
    prev_lines = [pattern[0]]
    for idx, line in enumerate(pattern[1:]):
        cursor = idx + 1
        if excl and cursor == excl["index"] and dir == excl["mode"]:
            prev_lines.append(line)
            continue

        if sum(1 for a, b in zip(line, prev_lines[-1]) if a != b) <= leniency:
            line_count = min(len(prev_lines), len(pattern[cursor:]))
            rest = pattern[cursor : cursor + line_count]
            prev = prev_lines[::-1][:line_count]

            if sum(1 for x, y in zip(rest, prev) for i, j in zip(x, y) if i != j) <= leniency:
                return cursor

        prev_lines.append(line)
    return -1


pattern = []
idx_1, idx_2 = 0, 0
for idx, line in enumerate(a):
    if line == "" or idx == len(a) - 1:
        found = {}
        index = find_reflection(pattern, 0, "horizontal")
        if index < 0:
            rotated = ["".join(list(reversed(col))) for col in zip(*pattern)]
            index = find_reflection(rotated, 0, "vertical")
            idx_1 += index
            found["mode"] = "vertical"
        else:
            idx_1 += index * 100
            found["mode"] = "horizontal"
        found["index"] = index

        index = find_reflection(pattern, 1, "horizontal", found)
        if index < 0:
            rotated = ["".join(list(reversed(col))) for col in zip(*pattern)]
            index = find_reflection(rotated, 1, "vertical", found)
            idx_2 += index
        else:
            idx_2 += index * 100
        pattern = []
    else:
        pattern.append(line)

print(f"Part 1: {idx_1}")
print(f"Part 2: {idx_2}")
