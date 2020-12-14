import math
import re

#read data
current_day = 'day14'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

def all_memory_addresses(memory_string):
    number_addresses = 2 ** memory_string.count('X')
    format_number = memory_string.count('X')
    format_string = '{0:0'+str(format_number)+'b}'
    replacements = []
    for i in range(0,number_addresses):
        new_mem_string = [char for char in memory_string]
        ex_replacement = format_string.format(i)
        for i in ex_replacement:
            new_mem_string[new_mem_string.index('X')] = i
        replacements.append(''.join(new_mem_string))
    return replacements


def solve_day14(data_in, part_number):
    print(f'\nPart {part_number}: ')
    memory = {}
    mask = None
    for instruction in data_in:
        if instruction[0:4] == 'mask':
            mask = [char for char in instruction[7:]]
        else:
            mem_address = int(re.findall(r'(?<=\[)[0-9].*(?=\])', instruction)[0])
            mem_update = int(re.findall(r'(?<=\= )[0-9].*', instruction)[0])
            
            if part_number == 1:
                mem_bits = [int(char) for char in '{0:036b}'.format(mem_update)]
                for idx, bit in enumerate(mem_bits):
                    mem_bits[idx] = str(bit) if mask[idx] == 'X' else mask[idx]
                
                mem_decimal = int(''.join(mem_bits),2)
                memory.update({mem_address:mem_decimal})
                
            elif part_number == 2:
                address_bits = [int(char) for char in '{0:036b}'.format(mem_address)]
                for idx, bit in enumerate(address_bits):
                    address_bits[idx] = str(bit) if mask[idx] == '0' else mask[idx]

                addresses = all_memory_addresses(''.join(address_bits))
                for i in addresses:
                    memory.update({i:mem_update})

    print(f'final total in memory: {sum(memory.values())}')


#Part 1
solve_day14(data_in, 1)

#Part 2
solve_day14(data_in, 2)
