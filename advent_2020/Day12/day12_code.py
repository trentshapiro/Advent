import numpy as np

#read data
current_day = 'day12'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

def move_direction(point, heading, amount):
    dir = {'N':(0,1),'S':(0,-1),'E':(1,0), 'W':(-1,0)}
    new_x = point[0] + (dir[heading][0] * amount)
    new_y = point[1] + (dir[heading][1] * amount)
    return (new_x, new_y)
    
def change_facing(start_dir, turn_dir, amount):
    right_dir = {'N':'E','E':'S','S':'W','W':'N'}
    left_dir = {'N':'W','W':'S','S':'E','E':'N'}
    num_turns = amount // 90
    new_dir = start_dir
    for i in range(0,num_turns):
        new_dir = left_dir[new_dir] if turn_dir == 'L' else right_dir[new_dir]
    return new_dir

def move_ship(waypoint, ahip, amount):
    wp_x, wp_y = waypoint
    ship_x, ship_y = ship
    x_mov = amount*(wp_x - ship_x)
    y_mov = amount*(wp_y - ship_y)
    return (ship_x+x_mov, ship_y+y_mov), (wp_x+x_mov, wp_y+y_mov)

def rotate_waypoint(wp, ship, direction, amount):
    angle = np.deg2rad(-1 * amount) if direction == 'L' else np.deg2rad(amount)
    cos_rad, sin_rad = (np.cos(angle), np.sin(angle))
    qx = ship[0] +  cos_rad * (wp[0] - ship[0]) + sin_rad * (wp[1] - ship[1])
    qy = ship[1] + -sin_rad * (wp[0] - ship[0]) + cos_rad * (wp[1] - ship[1])
    return (int(round(qx)), int(round(qy)))

#Part 1
facing = 'E'
ship = (0,0)
for i in data_in:
    action = str(i[0])
    amount = int(i[1:])
    if action in ('N','S','E','W'):
        ship = move_direction(ship, action, amount)
    elif action == 'F':
        ship = move_direction(ship, facing, amount)
    elif action in ('L','R'):
        facing = change_facing(facing, action, amount)

print('Part 1: ')
print(f'manhattan distance: {abs(ship[0])+abs(ship[1])}')


#Part 2
ship = (0,0)
waypoint = (10,1)
for i in data_in:
    action = str(i[0])
    amount = int(i[1:])
    if action in ('N','S','E','W'):
        waypoint = move_direction(waypoint, action, amount)
    elif action == 'F':
        ship, waypoint = move_ship(waypoint, ship, amount)
    elif action in ('L','R'):
        waypoint = rotate_waypoint(waypoint, ship, action, amount)
    
print('\nPart 2:')
print(f'manhattan distance: {abs(ship[0])+abs(ship[1])}')