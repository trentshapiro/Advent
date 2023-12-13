from functools import cache

with open("day12_input.txt") as f:
    a = f.readlines()
    a = [i.replace("\n", "") for i in a]


@cache
def check_string(i_str: str, i_groups: tuple[int]) -> int:
    if len(i_groups) == 0:
        if "#" in i_str:
            return 0
        else:
            return 1

    if sum(i_groups) + len(i_groups) - 1 > len(i_str):
        return 0

    if i_str[0] == ".":
        return check_string(i_str[1:], i_groups)

    broken = 0
    if i_str[0] == "?":
        broken += check_string(i_str[1:], i_groups)

    if "." in i_str[: i_groups[0]]:
        return broken

    if len(i_str) <= i_groups[0] or i_str[i_groups[0]] != "#":
        broken += check_string(i_str[i_groups[0] + 1 :], i_groups[1:])

    return broken


total_valid = 0
total_valid_2 = 0
for line in a:
    i_str, i_groups = line.split(" ")
    i_groups = [int(i) for i in i_groups.split(",")]
    total_valid += check_string(i_str, tuple(i_groups))

    i_groups_2 = i_groups * 5
    i_str_2 = "?".join([i_str] * 5)
    total_valid_2 += check_string(i_str_2, tuple(i_groups_2))

print(f"part 1: {total_valid}")
print(f"part 2: {total_valid_2}")
