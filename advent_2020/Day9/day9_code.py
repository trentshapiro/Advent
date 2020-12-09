# read data
current_day = 'day9'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [int(i.replace('\n','')) for i in data_in]

#Part 1
print('PART 1: ')
repeat_value = 0
window_size = 25
for i in range(0,len(data_in) - window_size):
    prev = data_in[i:i+window_size]
    current_value = data_in[i+window_size]
    pairs = set([j+k for j in prev for k in prev if j!=k])
    if current_value not in pairs:
        print('INVALID NUMBER FOUND:', current_value)
        repeat_value = current_value
        break


#Part 2
print('\nPART 2: ')
contiguous_set = None
found_flag = False
for set_length in range(2,30):
    for i in range(0,len(data_in) - set_length):
        if sum(data_in[i:i+set_length]) == repeat_value:
            found_flag = True
            contiguous_set = data_in[i:i+set_length]
            print('CONTIGUOUS SET FOUND OF LENGTH:', set_length)
            print('ENCRYPTION WEAKNESS:', min(contiguous_set)+max(contiguous_set))
            break
    if found_flag:
        break
