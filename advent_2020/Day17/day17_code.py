from copy import deepcopy

#read data
current_day = 'day17'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

starting_grid = [[1 if char == '#' else 0 for char in i] for i in data_in]


#Part 1
def print_space(input_space):
    for idx,i in enumerate(input_space):
        print(f'x={idx}')
        for j in i:
            print(j)

def sum_space(input_space):
    return sum([sum([sum(i) for i in slice]) for slice in input_space])
    

def expand_space(input_space):
    output_space = []
    for slice in input_space:
        new_rows = []
        for row in slice:
            new_row = [0]+row+[0]
            new_rows.append(new_row)
        
        new_slice_pad = [0 for i in range(0, len(new_rows[0]))]
        new_slice = [new_slice_pad] + new_rows + [new_slice_pad]
        output_space.append(new_slice)
    
    x_expansion = [[0 for i in range(0,len(output_space[0][0]))] for j in range(0,len(output_space[0]))]
    output_space = [x_expansion] + output_space + [x_expansion]
    return output_space


def evolve_point(input_space, point):
    directions = [(i,j,k) for i in range(-1,2) for j in range(-1,2) for k in range(-1,2) if (i,j,k) != (0,0,0)]
    x,y,z = point
    current_state = input_space[x][y][z]
        
    count_alive = 0
    for neighbor in directions:
        x2,y2,z2 = neighbor
        x_check = x+x2>0 and x+x2<len(input_space)
        y_check = y+y2>0 and y+y2<len(input_space[0])
        z_check = z+z2>0 and z+z2<len(input_space[0][0])
        
        if x_check and y_check and z_check:
            neighbor_val = input_space[x+x2][y+y2][z+z2]
            count_alive+=neighbor_val
        else:
            count_alive+=0

    if current_state == 1:
        if count_alive == 2 or count_alive == 3:
            final_state = 1
        else:
            final_state = 0
    elif current_state == 0:
        if count_alive == 3:
            final_state = 1
        else:
            final_state = 0

    return final_state


def evolve_space(input_space):
    output_space = []
    for i in range(0,len(input_space)):
        new_grid = []
        for j in range(0,len(input_space[0])):
            new_row = []
            for k in range(0, len(input_space[0][0])):
                this_point = (i,j,k)
                new_state = evolve_point(input_space, this_point)
                new_row.append(new_state)
            new_grid.append(new_row)
        output_space.append(new_grid)
    return output_space


print('PART 1: ')
current_space = [deepcopy(starting_grid)]
for i in range(0,6):
    current_space = expand_space(current_space)
    current_space = evolve_space(current_space)

total_on = sum_space(current_space)
print(total_on)


#Part 2
def sum_space_4d(input_n):
    return sum([sum([sum([sum(i) for i in slice]) for slice in input_space]) for input_space in input_n])
    
def expand_space_4d(input_n):
    output_n = []
    for space in input_n:
        output_space = []
        for slice in space:
            new_rows = []
            for row in slice:
                new_row = [0]+row+[0]
                new_rows.append(new_row)
            
            new_slice_pad = [0 for i in range(0, len(new_rows[0]))]
            new_slice = [new_slice_pad] + new_rows + [new_slice_pad]
            output_space.append(new_slice)

        space_expansion = [[0 for i in range(0,len(output_space[0][0]))] 
                              for j in range(0,len(output_space[0]))]
        output_n.append([space_expansion] + output_space + [space_expansion])
        
    output_n_expansion = [[[0 for i in range(0,len(output_n[0][0][0]))] 
                              for j in range(0,len(output_n[0][0]))] 
                              for k in range(0,len(output_n[0]))]
    
    output_n = [output_n_expansion] + output_n + [output_n_expansion]
    return output_n


def evolve_point_4d(input_space, point):
    directions = [(i,j,k,l) for i in range(-1,2) for j in range(-1,2) \
                    for k in range(-1,2) for l in range(-1,2) if (i,j,k,l) != (0,0,0,0)]
    x,y,z,w = point
    current_state = input_space[x][y][z][w]
        
    count_alive = 0
    for neighbor in directions:
        x2,y2,z2,w2 = neighbor
        x_check = x+x2>0 and x+x2<len(input_space)
        y_check = y+y2>0 and y+y2<len(input_space[0])
        z_check = z+z2>0 and z+z2<len(input_space[0][0])
        w_check = w+w2>0 and w+w2<len(input_space[0][0][0])
        
        if x_check and y_check and z_check and w_check:
            neighbor_val = input_space[x+x2][y+y2][z+z2][w+w2]
            count_alive+=neighbor_val
        else:
            count_alive+=0

    if current_state == 1:
        if count_alive == 2 or count_alive == 3:
            final_state = 1
        else:
            final_state = 0
    elif current_state == 0:
        if count_alive == 3:
            final_state = 1
        else:
            final_state = 0
    else:
        print(current_state)
        return None

    return final_state


def evolve_space_4d(input_space):
    output_n = []
    for i in range(0,len(input_space)):
        new_space = []
        for j in range(0,len(input_space[0])):
            new_grid = []
            for k in range(0, len(input_space[0][0])):
                new_row = []
                for l in range(0, len(input_space[0][0][0])):
                    this_point = (i,j,k,l)
                    new_state = evolve_point_4d(input_space, this_point)
                    new_row.append(new_state)
                new_grid.append(new_row)
            new_space.append(new_grid)
        output_n.append(new_space)
    return output_n


print('\nPart 2:')
current_space = [[deepcopy(starting_grid)]]
for i in range(0,6):
    current_space = expand_space_4d(current_space)
    current_space = evolve_space_4d(current_space)

total_on = sum_space_4d(current_space)
print(total_on)