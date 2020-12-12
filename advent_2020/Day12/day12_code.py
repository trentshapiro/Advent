import numpy as np

#read data
current_day = 'day12'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

def move_direction(x, y, heading, amount):
    if heading == 'N':
        y += amount
    elif heading == 'S':
        y -= amount
    elif heading == 'E':
        x += amount
    elif heading == 'W':
        x -= amount
    return x, y
    
def change_facing(start_dir, turn_dir, amount):
    right_dir = {'N':'E','E':'S','S':'W','W':'N'}
    left_dir = {'N':'W','W':'S','S':'E','E':'N'}
    num_turns = amount // 90
    new_dir = start_dir
    for i in range(0,num_turns):
        if turn_dir == 'L':
            new_dir = left_dir[new_dir]
        elif turn_dir == 'R':
            new_dir = right_dir[new_dir]
    return new_dir


#Part 1
facing = 'E'
ship_x = 0
ship_y = 0

for i in data_in:
    action = str(i[0])
    amount = int(i[1:])
    
    if action in ('N','S','E','W'):
        ship_x, ship_y = move_direction(ship_x, ship_y, action, amount)
    elif action == 'F':
        ship_x, ship_y = move_direction(ship_x, ship_y, facing, amount)
    elif action in ('L','R'):
        facing = change_facing(facing, action, amount)
print('Part 1: ')
print('final x, final y')
print(ship_x, ship_y)
print(f'manhattan distance: {abs(ship_x)+abs(ship_y)}')


#part 2
def move_ship(wp_x, wp_y, ship_x, ship_y, amount):
    x_mov = amount*(wp_x - ship_x)
    y_mov = amount*(wp_y - ship_y)
    return ship_x+x_mov, ship_y+y_mov, wp_x+x_mov, wp_y+y_mov

def rotate_waypoint(wp_x, wp_y, ship_x, ship_y, direction, amount):
    if direction == 'L':
        amount = -1 * amount
    
    offset_x = ship_x
    offset_y = ship_y
    x = wp_x
    y = wp_y
    
    radians = np.deg2rad(amount)
    adjusted_x = (x - offset_x)
    adjusted_y = (y - offset_y)
    cos_rad = np.cos(radians)
    sin_rad = np.sin(radians)
    qx = offset_x + cos_rad * adjusted_x + sin_rad * adjusted_y
    qy = offset_y + -sin_rad * adjusted_x + cos_rad * adjusted_y
    return int(round(qx)), int(round(qy))

ship_x = 0
ship_y = 0
wp_x = 10
wp_y = 1

for i in data_in:
    action = str(i[0])
    amount = int(i[1:])
    if action in ('N','S','E','W'):
        wp_x, wp_y = move_direction(wp_x, wp_y, action, amount)
    elif action == 'F':
        ship_x, ship_y, wp_x, wp_y = move_ship(wp_x, wp_y, ship_x, ship_y, amount)
    elif action in ('L','R'):
        wp_x, wp_y = rotate_waypoint(wp_x, wp_y, ship_x, ship_y, action, amount)
    
print('\nPart 2:')
print('final x, final y')
print(ship_x, ship_y)
print(f'manhattan distance: {abs(ship_x)+abs(ship_y)}')