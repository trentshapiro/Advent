current_day = 'day5'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]


#binary splitter
def half_list(list_in,which_half):
    half_point = int(len(list_in)/2)
    if which_half == 'lower':
        return list_in[0:half_point]
    elif which_half == 'upper':
        return list_in[half_point:len(list_in)]


seat_ids = []
row_list = list(range(0,128))
col_list = list(range(0,8))

for seat in data_in:
    current_row = row_list
    current_col = col_list
    
    row_half_list = seat[0:-3]
    for row_half in row_half_list:
        if row_half == 'F':
            current_row = half_list(current_row, 'lower')
        elif row_half == 'B':
            current_row = half_list(current_row, 'upper')
    
    col_half_list = seat[-3:]
    for col_half in col_half_list:
        if col_half == 'L':
            current_col = half_list(current_col, 'lower')
        elif col_half == 'R':
            current_col = half_list(current_col, 'upper')
    
    seat_ids.append(current_row[0]*8 + current_col[0])

#part 1
max_seat_id = max(seat_ids)
print(max_seat_id)

#part 2
min_seat_id = min(seat_ids)
seat_range = list(range(min_seat_id, max_seat_id))
missing = [i for i in seat_range if i not in seat_ids]


print(missing[0])