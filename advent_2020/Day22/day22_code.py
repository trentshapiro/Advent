from copy import deepcopy

#read data
current_day = 'day22'
with open(current_day+'_input.txt','r') as f:
    data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

#part 1
def sim_round(p1, p2):
    p1_card = p1[0]
    p2_card = p2[0]

    if p1_card > p2_card:
        p2 = p2[1:]
        p1 = p1[1:]+[p1_card]+[p2_card]
    elif p2_card > p1_card:
        p1 = p1[1:]
        p2 = p2[1:]+[p2_card]+[p1_card]

    return p1, p2

def sim_game(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        p1, p2 = sim_round(p1,p2)

    return p1, p2

print('Part 1: ')
p1 = [int(i) for i in data_in[1:26]]
p2 = [int(i) for i in data_in[28:]]

p1, p2 = sim_game(p1,p2)
winner_name = 'p1' if p1 != [] else 'p2'
winner = p1 if p1 != [] else p2
winner_score = sum([x*y for x,y in zip(winner,[i for i in range(1,len(winner)+1)][::-1])])
print(f'winner is {winner_name}')
print(f'winner score is {winner_score}')

#part 2
def sim_round_2(p1, p2):
    p1_card = p1[0]
    p2_card = p2[0]

    p1 = p1[1:]
    p2 = p2[1:]
    
    #sub game condition
    if len(p1)>= p1_card and len(p2)>=p2_card:
        p1_subdeck = p1[0:p1_card]
        p2_subdeck = p2[0:p2_card]
        winner, _, _ = sim_game_2(p1_subdeck, p2_subdeck)
    else:
        winner = 'p1' if p1_card > p2_card else 'p2'
    
    if winner == 'p1':
        p2 = p2
        p1 = p1+[p1_card]+[p2_card]
    elif winner == 'p2':
        p1 = p1
        p2 = p2+[p2_card]+[p1_card]
    
    return winner, p1, p2

def sim_game_2(p1, p2):
    p1_hist = []
    p2_hist = []

    while p1 != [] and p2 != []:
        p1_prev = p1
        p2_prev = p2

        if p1 in p1_hist or p2 in p2_hist:
            winner = 'p1'
            break

        winner, p1, p2 = sim_round_2(p1, p2)

        p1_hist.append(p1_prev)
        p2_hist.append(p2_prev)
    
    return winner, p1, p2

#part 2
print('\nPart 2: ')
p1 = [int(i) for i in data_in[1:26]]
p2 = [int(i) for i in data_in[28:]]
winner_name, p1, p2 = sim_game_2(p1,p2)
winner = p1 if winner_name == 'p1' else p2
winner_score = sum([x*y for x,y in zip(winner,[i for i in range(1,len(winner)+1)][::-1])])
print(f'winner is {winner_name}')
print(f'winner score is {winner_score}')