import re

with open("day03_input.txt") as f:
    a = f.readlines()
    a = [i.replace('\n','') for i in a]

MASK = [
    (-1,-1) ,(-1,0) ,(-1,1),
    ( 0,-1) ,( 0,0) ,( 0,1),
    ( 1,-1) ,( 1,0) ,( 1,1),
]

MAX_X = len(a[0])
MAX_Y = len(a)


def apply_mask(row_number, input_range):
    points_to_check = []
    for i in range(input_range[0],input_range[1]):
        for mask_x, mask_y in MASK:
            new_x = row_number+mask_x
            new_y = i+mask_y
            if new_x >= 0 and new_x < MAX_X and new_y >= 0 and new_y < MAX_Y:
                points_to_check.append((new_x,new_y))
    return points_to_check

#part 1
valid_total = 0
for row_number, row in enumerate(a):
    number_positions = [i.span() for i in re.finditer("[0-9]{1,3}",row)]

    if len(number_positions) == 0:
        continue

    for position in number_positions:
        position_values = [a[x][y] for (x,y) in apply_mask(row_number, position)]
        check_chars = [i for i in position_values if not i.isnumeric() and i != "."]
        if len(check_chars) > 0:
            number_value = int(row[position[0]:position[1]])
            valid_total += number_value

print(valid_total)

#part 2
sum_ratios = 0
for row_number, row in enumerate(a):
    star_positions = [i.span() for i in re.finditer(r"\*",row)]

    if len(star_positions) == 0:
        continue

    for position in star_positions:
        position_values = [a[x][y] for (x,y) in apply_mask(row_number, position)]
        
        touch_numbers = []
        left_pos = position[0]-1
        right_pos = position[1]+1

        for idx in range(0,3):
            row_values = [i.span() for i in re.finditer("[0-9]{1,3}",a[row_number+idx-1])]
            for span in row_values:
                if (span[0] in range(left_pos,right_pos) or 
                    span[1]-1 in range(left_pos,right_pos)):
                    touch_numbers.append(int(a[row_number+idx-1][span[0]:span[1]]))

        if len(touch_numbers) == 2:
            sum_ratios = sum_ratios + (touch_numbers[0]*touch_numbers[1])

print(sum_ratios)