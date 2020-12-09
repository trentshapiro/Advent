# read data
current_day = 'day9'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [int(i.replace('\n','')) for i in data_in]

#Part 1
print('PART 1: ')
repeat_value = 0
for idx, value in enumerate(data_in[25:]):
    prev = data_in[idx:idx+25]
    current_value = value      
    pairs = set([i+j for i in prev for j in prev if i!=j])
    if current_value not in pairs:
        print('value not in pairs found! ', current_value)
        repeat_value = current_value
        break


#Part 2
print('\nPART 2: ')
contiguous_set = None
found_flag = False
for set_length in range(2,30):
    for idx, value in enumerate(data_in[idx:]):
        if sum(data_in[idx:idx+set_length]) == repeat_value:
            print('CONTIGUOUS SET FOUND OF LENGTH', set_length)
            contiguous_set = data_in[idx:idx+set_length]
            found_flag = True
            print('Sum of min and max:', min(contiguous_set)+max(contiguous_set))
            break

