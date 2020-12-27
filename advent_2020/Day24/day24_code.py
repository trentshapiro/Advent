from copy import deepcopy
#read data
current_day = 'day24'
with open(current_day+'_input.txt','r') as f:
   data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

dir_transform = {
    'w': (-1, 1, 0),
    'e': ( 1,-1, 0),
    'nw':( 0, 1,-1),
    'se':( 0,-1, 1),
    'ne':( 1, 0,-1),
    'sw':(-1, 0, 1)
}

def follow_path(start_pos, directions):
    x,y,z = start_pos
    for direction in directions:
        d_x,d_y,d_z = dir_transform[direction]
        x+=d_x
        y+=d_y
        z+=d_z
    return str((x,y,z))

def expand_dict(hex_dict):
    dict_out = {}

    for key in hex_dict.keys():
        x,y,z = eval(key)
        current_state = hex_dict[key]
        dict_out.update({key:current_state})

        for adj in dir_transform.keys():
            d_x, d_y, d_z = dir_transform[adj]
            new_key = str((x+d_x,y+d_y,z+d_z))
            if new_key not in hex_dict:
                dict_out.update({new_key:0})
    return dict_out

def update_dict(hex_dict):
    dict_out = {}

    for key in hex_dict.keys():
        x,y,z = eval(key)
        current_state = hex_dict[key]

        count_black = 0
        for adj in dir_transform.keys():
            d_x, d_y, d_z = dir_transform[adj]
            new_key = str((x+d_x,y+d_y,z+d_z))
            adj_state = hex_dict[new_key] if new_key in hex_dict else 0
            count_black += adj_state
        
        if current_state == 1:
            new_state = 0 if count_black == 0 or count_black > 2 else 1
        else:
            new_state = 1 if count_black == 2 else 0
        
        dict_out.update({key:new_state})
    return dict_out


#Part 1
directions_in = []
for i in data_in:
    list_out = []
    temp_list = [char for char in i]
    while len(temp_list) > 0:
        this_char = temp_list.pop(0)
        if this_char in ('s', 'n'):
            direction = this_char + temp_list.pop(0)
        else:
            direction = this_char
        list_out.append(direction)
    directions_in.append(list_out)

status_dict = {}
for path in directions_in:
    start_pos = (0,0,0)
    final_pos = follow_path(start_pos, path)
    
    if final_pos in status_dict.keys():
        current_status = status_dict[final_pos]
    else:
        current_status = 0
    
    new_status = 1 - current_status
    status_dict.update({final_pos:new_status})

print('Part 1: ')
print(f'number of instructions: {len(directions_in)}')
print(f'total number of traveled tiles: {len(status_dict.keys())}')
print(f'total number of remaining black tiles: {sum(status_dict.values())}')


#Part 2
hex_dict = deepcopy(status_dict)
for i in range(0,100):
    hex_dict = expand_dict(hex_dict)
    hex_dict = update_dict(hex_dict)

print('/Part 2: ')
print(f'total number of remaining black tiles: {sum(hex_dict.values())}')
