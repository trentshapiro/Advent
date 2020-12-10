import re


current_day = 'day7'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

# generate dictionary of rules
rules_dict = {}
for rule in data_in:
    
    container = rule.split(' bags contain ')[0]
    insides = rule.split(' bags contain ')[1]
    
    if insides == 'no other bags.':
        insides = ['None']
    else:
        insides = insides.replace('.','').split(', ')
        
    container = container.replace(' bags','')
    insides = [i.replace(' bags','').replace(' bag','') for i in insides]
    
    
    rules_dict.update({container:insides})


#Part 1
#bottom up
def check_contents(target_list):
    contain_target = []
    
    for i in rules_dict.keys():
        container = i
        insides = rules_dict[i]
        
        for bag in insides:
            for target in target_list:
                if target in bag:
                    contain_target.append(i)
    
    return contain_target
    
 

target_bag = ['shiny gold']

previous_bags = list(set(check_contents(target_bag)))
total_bags = previous_bags

while 1:
    current_list = list(set(check_contents(previous_bags)))
    new_bags = [i for i in current_list if i not in total_bags]
    
    if new_bags != []:
        total_bags = total_bags + new_bags
        previous_bags = new_bags
    else:
        break

print('Total Containing Shiny Gold: ', len(total_bags))

#Part 2
#top down
def bags_inside(bag):
    count = 0
    if bag == 'None':
        return count
    contents = rules_dict[bag]
    for entry in contents:
        if entry == 'None':
            continue
        else:
            num_bags = int(re.findall(r'[0-9]',entry)[0])
            bag_name = re.findall(r'(?<=[0-9] ).*',entry)[0]
            count = count + num_bags + (num_bags*bags_inside(bag_name))
    return count


print('Bags Contained Inside Shiny Gold: ', bags_inside(target_bag[0]))