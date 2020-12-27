#read data
current_day = 'day25'
with open(current_day+'_input.txt','r') as f:
    data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]


def transform_key(loops, key, divisor, subject=1):
    while loops > 0:
        subject = (subject * key) % divisor
        loops-=1
    return subject

def find_loop(key, key_target, divisor, subject=1):
    loops = 1
    while True:
        subject = (subject * key) % divisor
        if subject == key_target:
            return loops
        loops+=1
    return -1


door_key_target = int(data_in[0])
card_key_target = int(data_in[1])
starting_key = 7
divisor = 20201227

door_loops = find_loop(starting_key, door_key_target, divisor)
card_loops = find_loop(starting_key, card_key_target, divisor)
enc_key = transform_key(card_loops, door_key_target, divisor, 1)

print(f'door pub key {door_key_target}')
print(f'door key loops {door_loops}')
print(f'card pub key {card_key_target}')
print(f'card key loops {card_loops}')
print(f'encryption key {enc_key}')