import numpy as np

# read data
current_day = 'day10'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [int(i.replace('\n','')) for i in data_in]

#Part 1
print('PART 1:')
max_v = max(data_in)+3
volt_list = [0] + sorted(data_in) + [max_v]
diffs = [volt_list[i]-volt_list[i-1] for i in range(1, len(volt_list))]
print(diffs.count(1) * diffs.count(3))


#part 2
print('\nPART 2:')

children_dict = {}
for i in volt_list:
    children_dict.update({
        i:[j for j in volt_list if j-i in (1,2,3)]
    })

#store number values we already calculated
numbers_searched = {}

#find all roots
def find_root(starting_node):
    children = children_dict[starting_node]
    final_value = 0
    
    #count when we hit the final node, otherwise get children
    if children == []:
        return 1
    else:
        for child in children:
            #if we've already calulated downstream, cool, otherwise calculate
            if child in numbers_searched.keys():
                child_value = numbers_searched[child]
            else:
                child_value = find_root(child)
                numbers_searched.update({child:child_value})
            final_value += child_value
    return final_value

final_value = find_root(0)
print(final_value)