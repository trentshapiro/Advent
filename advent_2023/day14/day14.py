import numpy as np

with open("day14_input.txt") as f:
    a = f.readlines()
    a = tuple([tuple(i.replace("\n", "")) for i in a])


def sort_row(input_row: tuple):
    sub_row = ["".join(sorted(i)) for i in "".join(input_row).split("#")]
    return tuple("#".join(sub_row))


def spin(input_mat: tuple[tuple[str]], rotate: bool) -> list[str]:
    output_mat = np.array(input_mat)
    output_mat = np.rot90(output_mat, 3)
    output_mat = np.array(tuple(sort_row(tuple(i)) for i in output_mat))

    if rotate:
        for _ in range(3):
            output_mat = np.rot90(output_mat, 3)
            output_mat = np.array(tuple(sort_row(tuple(i)) for i in output_mat))
    else:
        output_mat = np.rot90(output_mat, 1)

    return tuple(map(tuple, output_mat))


def mat_value(x) -> int:
    return sum(sum(len(x) - idx for i in row if i == "O") for idx, row in enumerate(x))


# 1
slid = spin(a, False)
print(f"Part 1: {mat_value(slid)}")

# 2
prev_states = [a]
for i in range(1, 1_000_000_000):
    state = spin(prev_states[-1], rotate=True)
    if state not in prev_states:
        prev_states.append(state)
    else:
        relevant_states = prev_states[prev_states.index(state) :]
        final_cycle = (1_000_000_000 - i + 1) % len(relevant_states)
        final_state = relevant_states[final_cycle - 1]
        break

print(f"Part 2: {mat_value(final_state)}")
