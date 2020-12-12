import itertools

#read data
current_day = 'day11'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

#8 directional count empty and full
def check_direction(board, point, heading, search_len):
    #all traversable directions
    compass = [i for i in list(itertools.product(range(-1,2),range(-1,2))) if i != (0,0)]
    
    #this specific direction
    search_dir = compass[heading]
    
    #search in given direction until hitting # or L for given distance
    for i in range(1,search_len+1):
        new_x = point[0]+(search_dir[0]*i)
        new_y = point[1]+(search_dir[1]*i)
        
        if (0<=new_x<=max_row) and (0<=new_y<=max_col):
            value = board[new_x][new_y]
            if value == '#':
                return 'full'
            elif value == 'L':
                return 'empty'
            else:
                pass
        else:
            return 'clear'

#game board update
def new_board(board, search_len, full_threshold):
    output_board = []
    for row_idx in range(0,len(board)):
        output_row = []
        for col_idx in range(0,len(board[0])):
            current_state = board[row_idx][col_idx]
            if current_state == '.':
                output_row.append('.')
            else:
                point = (row_idx,col_idx)
                full = [check_direction(board, point, i, search_len) for i in range(0,8)].count('full')
                if current_state == 'L' and full == 0:
                    output_row.append('#')
                elif current_state == '#' and full >= full_threshold:
                    output_row.append('L')
                else:
                    output_row.append(current_state)   
                  
        output_board.append(output_row)
    return output_board

#iterate
def final_board(board, prev_board, search_len, full_threshold):
    while board != prev_board:
        prev_board = board
        board = new_board(prev_board, search_len, full_threshold)
    return sum([i.count('#') for i in board])

#set up
starting_board = [[char for char in i] for i in data_in]
max_col = len(starting_board[0]) - 1
max_row = len(starting_board) - 1

#Part 1
print('PART 1: ')
print(final_board(starting_board, [], 1, 4))


#Part 2
print('\nPart 2: ')
print(final_board(starting_board, [], 1000, 5))


