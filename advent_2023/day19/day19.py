from copy import deepcopy
from day19_part1 import rule_dict

xmas = {
    "x": [1, 4000],
    "m": [1, 4000],
    "a": [1, 4000],
    "s": [1, 4000],
}


def check_range(rule: str, xmas_range: dict[str, int]):
    # Accepted criteria
    if rule == "A":
        return [xmas_range]

    # Reject rule
    if rule == "R":
        return []

    # No valid range
    for i, j in xmas_range.values():
        if j - i <= 0:
            return []

    # Base case
    rules = rule_dict[rule]
    valid_ranges = []

    new_range = deepcopy(xmas_range)
    for rule in rules:
        letter = rule["source"]
        if rule["op"] == ">":
            # store initial
            inital_value = new_range[letter][0]

            # meets condition
            new_range[letter][0] = rule["comp"] + 1
            valid_ranges.extend(check_range(rule["target"], deepcopy(new_range)))

            # doesnt meet condition
            new_range[letter][0] = inital_value
            new_range[letter][1] = rule["comp"]

        elif rule["op"] == "<":
            # store initial
            inital_value = new_range[letter][1]

            # meets condition
            new_range[letter][1] = rule["comp"] - 1
            valid_ranges.extend(check_range(rule["target"], deepcopy(new_range)))

            # doesnt meet condition
            new_range[letter][1] = inital_value
            new_range[letter][0] = rule["comp"]
        else:
            valid_ranges.extend(check_range(rule["target"], deepcopy(new_range)))

    return valid_ranges


valid_ranges = check_range("in", xmas)
volume = 0
volume_added = []
for idx, xmas in enumerate(valid_ranges):
    # base volume
    base_volume = 1
    for k, v in xmas.items():
        base_volume *= v[1] - v[0] + 1

    # subtract overlaps
    mins = [i[0] for i in xmas.values()]
    maxs = [i[1] for i in xmas.values()]
    for prev_area in volume_added:
        prev_mins = [i[0] for i in prev_area.values()]
        prev_maxs = [i[1] for i in prev_area.values()]
        overlapping_area = max(min(maxs[0], prev_maxs[0]) - max(mins[0], prev_mins[0]), 0)
        for i in range(1, 4):
            overlapping_area *= max(min(maxs[i], prev_maxs[i]) - max(mins[i], prev_mins[i]), 0)
        base_volume -= overlapping_area

    # add area to checked areas
    volume_added.append(xmas)

    # increase total volume by non-overlapped volume
    volume += max(base_volume, 0)

print(f"Part 2: {volume}")
