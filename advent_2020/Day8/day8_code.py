# read data
current_day = 'day8'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

# execute arbitrary instructions :)
def run_program(instruction_set):
    already_operated_indices = []
    acc = 0
    cur_pos = 0
    
    while 1:
        if cur_pos > len(instruction_set)-1:
            return 'finished', acc
        operation = instruction_set[cur_pos]
        instruction = operation.split(' ')[0]
        increment = int(operation.split(' ')[1])
        
        #check if this index has been operated yet
        if cur_pos in already_operated_indices:
            return 'loop', acc
            break
        else:
            already_operated_indices.append(cur_pos)
            if instruction == 'nop':
                cur_pos += 1
            elif instruction == 'acc':
                acc += increment
                cur_pos += 1
            elif instruction == 'jmp':
                cur_pos += increment

#part 1
print('PART 1: ')
state, acc = run_program(data_in)
print(state, acc)
print('\n')

#part 2
print('PART 2: ')
for idx, operation in enumerate(data_in):
    
    instruction = operation.split(' ')[0]
    increment = operation.split(' ')[1]
    
    if instruction != 'acc':
        if instruction == 'nop':
            instruction = 'jmp'
        elif instruction == 'jmp':
            instruction = 'nop'
        else:
            continue
        
        new_value = ' '.join([instruction,increment])
        new_stream = data_in[0:idx]+[new_value]+data_in[idx+1:]
        
        state, acc = run_program(new_stream)
        
        if state == 'finished':
            print('found correct instruction to replace!')
            print('operation at ', idx ,' became a ', instruction)
            print('final accumulator value: ', acc)
            break


























