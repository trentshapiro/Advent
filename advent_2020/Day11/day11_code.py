import itertools

# read data
current_day = 'day11'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]


# 8 directional sight count empty and full
def full_or_empty_dir(board, x_idx, y_idx, direction, search_distance):
    if direction == 1:
        x_inc = -1
        y_inc = -1
    elif direction == 2:
        x_inc = -1
        y_inc =  1
    elif direction == 3:
        x_inc =  1
        y_inc =  1
    elif direction == 4:
        x_inc =  1
        y_inc = -1
    elif direction == 5:
        x_inc = -1
        y_inc =  0
    elif direction == 6:
        x_inc =  1
        y_inc =  0
    elif direction == 7:
        x_inc =  0
        y_inc = -1
    elif direction == 8:
        x_inc =  0
        y_inc =  1
    
    for i in range(1,search_distance+1):
        new_x = x_idx+(x_inc*i)
        new_y = y_idx+(y_inc*i)
        
        if (min_row<=new_x<=max_row) and (min_col<=new_y<=max_col):
            value = board[new_x][new_y]
            if value == '#':
                return 'full'
            elif value == 'L':
                return 'empty'
            else:
                pass
        else:
            return 'clear'


def ray_check_point(board, point, search_distance):
    x_idx = point[0]
    y_idx = point[1]
    
    seat_outcomes = []
    #up/down/left/right
    seat_outcomes.append(full_or_empty_dir(board, x_idx, y_idx, 5, search_distance))
    seat_outcomes.append(full_or_empty_dir(board, x_idx, y_idx, 6, search_distance))
    seat_outcomes.append(full_or_empty_dir(board, x_idx, y_idx, 7, search_distance))
    seat_outcomes.append(full_or_empty_dir(board, x_idx, y_idx, 8, search_distance))

    #diagonals
    seat_outcomes.append(full_or_empty_dir(board, x_idx, y_idx, 1, search_distance))
    seat_outcomes.append(full_or_empty_dir(board, x_idx, y_idx, 2, search_distance))
    seat_outcomes.append(full_or_empty_dir(board, x_idx, y_idx, 3, search_distance))
    seat_outcomes.append(full_or_empty_dir(board, x_idx, y_idx, 4, search_distance))

    count_full = seat_outcomes.count('full')
    count_empty = seat_outcomes.count('empty')
    return count_empty, count_full


def new_board(input_board, search_distance, full_threshold):
    output_board = []
    for row_idx, row_list in enumerate(input_board):
        output_row = []
        for col_idx, value in enumerate(row_list):
            current_state = value
            if current_state == '.':
                output_row.append('.')
            else:
                empty, full = ray_check_point(input_board, (row_idx,col_idx), search_distance)
                if current_state == 'L' and full == 0:
                    output_row.append('#')
                elif current_state == '#' and full >= full_threshold:
                    output_row.append('L')
                else:
                    output_row.append(current_state)   
                  
        output_board.append(output_row)
    return output_board


starting_board = [[char for char in i] for i in data_in]

max_col = len(starting_board[0]) - 1
max_row = len(starting_board) - 1
min_col = 0
min_row = 0

#Part 1
print('PART 1: ')
previous_board = []
current_board = starting_board

while previous_board != current_board:
    previous_board = current_board
    current_board = new_board(previous_board, 1, 4)

print('Steady state found!')
print(sum([i.count('#') for i in previous_board]))


#Part 2
print('\nPart 2: ')
previous_board = []
current_board = starting_board

while previous_board != current_board:
    previous_board = current_board
    current_board = new_board(previous_board, 1000, 5)

print('Steady state found!')
print(sum([i.count('#') for i in previous_board]))

