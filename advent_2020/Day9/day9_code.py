# read data
current_day = 'day9'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [int(i.replace('\n','')) for i in data_in]

#Part 1
print('PART 1: ')
repeat_value = 0
for idx, value in enumerate(data_in):
    if idx < 25:
        continue
    else:
        prev_code = data_in[idx-25:idx]

        current_value = value
        
        pairs = []
        for i in prev_code:
            for j in prev_code:
                if i != j:
                    pairs.append(i+j)
        
        pairs = list(set(pairs))
        if current_value not in pairs:
            print('value not in pairs found! ', current_value)
            repeat_value = current_value
            break


#Part 2
print('\nPART 2: ')
contiguous_set = None
found_flag = False
for set_length in range(2,30):
    if not found_flag:
        for idx, value in enumerate(data_in):
            if idx < set_length:
                continue
            elif sum(data_in[idx-set_length:idx]) == repeat_value:
                print('CONTIGUOUS SET FOUND OF LENGTH', set_length)
                contiguous_set = data_in[idx-set_length:idx]
                found_flag = True
                break
    else:
        break

print('Sum of min and max:', min(contiguous_set)+max(contiguous_set))
               
               
               
               
