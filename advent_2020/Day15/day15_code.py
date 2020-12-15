#read data
current_day = 'day15'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]
data_in = [int(i) for i in data_in[0].split(',')]



def play_game(starting_data, max_iter):
    idx = len(starting_data) - 1 
    final_number = starting_data
    recent_dict = {}
    
    #populate memory dict with initial values and turns {value:last_seen_turn}
    for idx,num in enumerate(final_number[:-1]):
        recent_dict.update({num:idx+1})

    #initialize turn_number and value
    turn_number = len(final_number)
    current_number = final_number[-1]
    
    
    while turn_number < max_iter:
        #if a value is in memory, get age, else 0
        if current_number in recent_dict.keys():
            age = turn_number - recent_dict[current_number]
        else:
            age = 0
        
        #update memory of current value to this turn
        recent_dict.update({current_number:turn_number})
        
        #update iterables
        current_number = age
        turn_number += 1
        
    return current_number

#Part 1
print(play_game(data_in, 2020))

#Part 1
print(play_game(data_in, 30000000))
