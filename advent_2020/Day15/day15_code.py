#read data
current_day = 'day15'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]
data_in = [int(i) for i in data_in[0].split(',')]

def play_game(number_list, max_turn):
    #initialize register, since values are all based on differences of turn numbers,
    #the maximum difference is the max_turn - first_turn, or max_turn - 1 
    register = [0 for i in range(0,max_turn-1)]
    
    #populate register with input list, initialize current value
    for idx,num in enumerate(number_list[:-1]):
        register[num] = idx+1
    current_number = number_list[-1]
    
    #play game from turn now to turn max
    for turn in range(len(number_list), max_turn):
        #if a value is in memory, get age, else 0
        register_value = register[current_number]
        age = turn - register_value if register_value>0 else 0
        
        #update memory of current value to this turn
        register[current_number] = turn
        
        #update iterables
        current_number = age
        
    return current_number

#Part 1
print(play_game(data_in, 2020))

#Part 1
print(play_game(data_in, 30000000))
