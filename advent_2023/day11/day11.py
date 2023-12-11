from itertools import combinations

with open("day11_input.txt") as f:
    a = f.readlines()
    a = [list(i.replace("\n","")) for i in a]

e_rows = [i for i in range(0,len(a)) if "#" not in a[i]]
e_cols = [i for i in range(0,len(a[0])) if '#' not in [row[i] for row in a]]

stars = []
for row_idx, row in enumerate(a):
    stars.extend([(row_idx, col_idx) for col_idx,val in enumerate(row) if val=="#"])

def calc_ds(mult):
    total_d = 0
    for (x1,y1),(x2,y2) in combinations(stars,2):
        x_rows = len([i for i in e_rows if i in range(min(x1,x2),max(x1,x2))])
        x_cols = len([i for i in e_cols if i in range(min(y1,y2),max(y1,y2))])
        total_d += (abs(x1-x2)+abs(y1-y2)) + (mult-1)*(x_cols+x_rows)
    return total_d

print(f"Part 1: {calc_ds(2)}")
print(f"Part 2: {calc_ds(1_000_000)}")