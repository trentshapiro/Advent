import re

#read data
current_day = 'day16'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

#format data in
filters_in = data_in[0:data_in.index('')]
my_ticket = [int(i) for i in data_in[data_in.index('your ticket:')+1].split(',')]
near_tickets = data_in[data_in.index('nearby tickets:')+1:]
near_tickets = [[int(j) for j in i.split(',')] for i in near_tickets]


#compile list of filters
filters = {}
for filter in filters_in:
    filter_split = re.split(r': |-| or ', filter)
    filter_name = filter_split[0].strip()
    filter_1_min = int(filter_split[1].strip())
    filter_1_max = int(filter_split[2].strip())
    filter_2_min = int(filter_split[3].strip())
    filter_2_max = int(filter_split[4].strip())
    filters.update({filter_name:[(filter_1_min,filter_1_max), (filter_2_min,filter_2_max)]})


#find all valid ticket numbers, dont see any filters >1000 or <0, lets go for that
valid_numbers = []
for i in range(0, 1000):
    if i in valid_numbers:
        continue
    else:
        for filter in filters.values():
            min_1, max_1 = filter[0]
            min_2, max_2 = filter[1]
            #find if the value is in any valid range
            if i in range(min_1,max_1+1) or i in range(min_2,max_2+1):
                valid_numbers.append(i)
                break

#find error values, and limit the nearby tickets to only valid
error_numbers = []
valid_near_tickets = []
for near_ticket in near_tickets:
    error_found = False
    for number in near_ticket:
        if number not in valid_numbers:
            error_numbers.append(number)
            error_found = True
            break
    if not error_found:
        valid_near_tickets.append(near_ticket)

#Part 1
print('Part 1: ')
print(sum(error_numbers))

#Part 2
print('\nPart 2: ')
valid_tickets = [my_ticket] + valid_near_tickets

valid_columns = []
for col in range(0,len(valid_tickets[0])):
    col_values = [i[col] for i in valid_tickets]
    valid_columns.append(col_values)

filters_w_cols = {}
for filter in filters.keys():
    filter_name = filter
    min_1, max_1 = filters[filter][0]
    min_2, max_2 = filters[filter][1]
    
    possible_columns = []
    for idx,col in enumerate(valid_columns):
        check = [i in range(min_1,max_1+1) or i in range(min_2,max_2+1) for i in col]
        if sum(check) == len(check):
            possible_columns.append(idx)
    
    filters_w_cols.update({filter_name:possible_columns})

final_pairings = {}
final_count = len(filters_w_cols.keys())
total_output = 1
while len(final_pairings) < final_count:
    for i in filters_w_cols.keys():
        if len(filters_w_cols[i]) == 1:
            col_number = filters_w_cols[i][0]
            print(f'col {col_number} = {i}')
            final_pairings.update({i: col_number})
            
            #remove value from other keys
            for j in filters_w_cols.keys():
                if col_number in filters_w_cols[j]:
                    new_list = filters_w_cols[j].remove(col_number)
                    
            #count if its one we care about
            if 'departure' in i:
                total_output = total_output*my_ticket[col_number]
            
            #remove this value from searchable list
            filters_w_cols.pop(i)
            break

    
print(total_output)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
