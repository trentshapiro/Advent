with open("day13_input.txt") as f:
    a = f.readlines()
    a = [i.replace("\n", "") for i in a]


def find_reflection(pattern: list[str]) -> int:
    prev_lines = [pattern[0]]
    for idx, line in enumerate(pattern[1:]):
        cursor = idx + 1
        if line == prev_lines[-1]:
            line_count = min(len(prev_lines), len(pattern[cursor:]))
            rest = pattern[cursor : cursor + line_count]
            prev = prev_lines[::-1][:line_count]
            if rest == prev:
                return cursor

        prev_lines.append(line)
    return -1


def find_smudged_reflection(
    pattern: list[str], check_type: str, exclusion: dict
) -> int:
    prev_lines = [pattern[0]]
    for idx, line in enumerate(pattern[1:]):
        cursor = idx + 1
        if cursor == exclusion["index"] and check_type == exclusion["mode"]:
            prev_lines.append(line)
            continue

        if sum(1 for a, b in zip(line, prev_lines[-1]) if a != b) <= 1:
            line_count = min(len(prev_lines), len(pattern[cursor:]))
            rest = pattern[cursor : cursor + line_count]
            prev = prev_lines[::-1][:line_count]

            if sum(1 for x, y in zip(rest, prev) for i, j in zip(x, y) if i != j) <= 1:
                return cursor

        prev_lines.append(line)
    return -1


pattern = []
idx_1, idx_2 = 0, 0
for idx, line in enumerate(a):
    if line == "" or idx == len(a) - 1:
        found_line_details = {}
        index = find_reflection(pattern)
        if index < 0:
            rotated = ["".join(list(reversed(col))) for col in zip(*pattern)]
            index = find_reflection(rotated)
            idx_1 += index
            found_line_details["mode"] = "vertical"
        else:
            idx_1 += index * 100
            found_line_details["mode"] = "horizontal"
        found_line_details["index"] = index

        index = find_smudged_reflection(pattern, "horizontal", found_line_details)
        if index < 0:
            rotated = ["".join(list(reversed(col))) for col in zip(*pattern)]
            index = find_smudged_reflection(rotated, "vertical", found_line_details)
            idx_2 += index
        else:
            idx_2 += index * 100
        pattern = []
    else:
        pattern.append(line)

print(f"Part 1: {idx_1}")
print(f"Part 2: {idx_2}")
