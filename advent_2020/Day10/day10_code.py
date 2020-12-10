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
class node:
    def __init__(self, name, parents, children):
        self.name = name
        self.parents = parents
        self.children = children
        self.num_children = len(children)
        self.num_parents = len(parents)

#create node network
nodes = []
for i in volt_list:
    name = i
    parents = [j for j in volt_list if i-j in (1,2,3)]
    children = [j for j in volt_list if j-i in (1,2,3)]
    nodes.append(node(i,parents,children))

#get a node value from its name
def get_node(name):
    return [i for i in nodes if i.name == name][0]

#store number values we already calculated
numbers_searched = {}

#find all roots
def find_root(starting_node):
    children = starting_node.children
    final_value = 0
    if children == []:
        return 1
    else:
        children_nodes = [get_node(i) for i in children]
        for node in children_nodes:
            if node.name in numbers_searched.keys():
                this_value = numbers_searched[node.name]
            else:
                this_value = find_root(node)
                numbers_searched.update({node.name:this_value})
            final_value += this_value
    return final_value

final_value = find_root(nodes[0])
print(final_value)