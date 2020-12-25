import time

#read data
current_day = 'day23'
with open(current_day+'_input.txt','r') as f:
    data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]


#Part 1
def take_turn(cup_list, max_value):
    current = cup_list.pop(0)
    picked_up = [cup_list.pop(0) for i in range(0,3)]    

    #find max value
    out_of_play = [current] + picked_up
    while max_value in out_of_play:
        max_value = max_value - 1

    target = current - 1
    if target < 1:
        target = max_value
    else:
        while target in out_of_play:
            target = target - 1
            if target < 1 :
                target = max_value
                break
    
    target_index = cup_list.index(target)+1
    cup_list[target_index:target_index] = picked_up
    cup_list.append(current) 
    return cup_list

def play_game(turns, cup_list):
    max_value = max(cup_list)
    for i in range(0, turns):
        cup_list = take_turn(cup_list, max_value)
    return cup_list

print('Part 1: ')
init_cup_config = [int(char) for char in data_in[0]]

final_cup_config = play_game(100, init_cup_config)
while final_cup_config[0] != 1:
    final_cup_config = final_cup_config[1:]+[final_cup_config[0]]
print('ouput right of 1: ')
print(''.join([str(i) for i in final_cup_config[1:]]))



#Part 2
def dict_take_turn(config_dict, current_value):
    #find the next 3 cups from current to pick up
    picked_up = []
    pickup_value = config_dict[current_value]
    for i in range(0,3):
        picked_up.append(pickup_value)
        pickup_value = config_dict[pickup_value]

    #find new target_value
    target_value = current_value - 1 if current_value > 1 else len(config_dict.keys())
    while target_value in [current_value]+picked_up:
        target_value = target_value - 1 if target_value > 1 else len(config_dict.keys())

    #get the value that target previously pointed to
    prev_target_point = config_dict[target_value]
    #get the value that came immediately after picked up cups
    prev_picked_up_point = config_dict[picked_up[-1]]

    #insert the picked up cups
    #target points to the first picked up cup
    config_dict.update({target_value:picked_up[0]})

    #the last picked up cup points to where target previously pointed to
    config_dict.update({picked_up[-1]:prev_target_point})

    #current now point to where picked up cups left a gap
    config_dict.update({current_value:prev_picked_up_point})

    #move to next point
    current_value = config_dict[current_value]

    return config_dict, current_value


def dict_play_game(turns, config_dict, current_value):
    for i in range(0,turns):
        config_dict, current_value = dict_take_turn(config_dict, current_value)
    
    return config_dict


init_cup_config = [int(char) for char in data_in[0]] + [i for i in range(10,1000001)]
start_number = init_cup_config[0]
config_dict = {}
for idx,i in enumerate(init_cup_config):
    try:
        config_dict.update({i:init_cup_config[idx+1]})
    except:
        config_dict.update({i:init_cup_config[0]})

print('\nPart 2: ')
starting_value = init_cup_config[0]
ending_dict = dict_play_game(10000000, config_dict, starting_value)
val_1 = ending_dict[1]
val_2 = ending_dict[val_1]
print(f'Next two values: {val_1} and {val_2}, multiplied = {val_1*val_2}')