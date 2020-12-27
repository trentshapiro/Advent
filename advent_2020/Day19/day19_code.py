#read data
current_day = 'day19'
with open(current_day+'_input.txt','r') as f:
   data_in = f.readlines()
data_in = [i.replace('\n','') for i in data_in]

def create_rules_dict(rules_list):
    dict_out = {}

    for line in rules_list:
        if line == '':
            continue
        rule_num = int(line.split(': ')[0])
        rule_val = line.split(': ')[1].replace('"','')

        if rule_val in ('a','b'):
            rule = rule_val
        else:
            rule = []
            for val in rule_val.split('|'):
                new_val = tuple([int(i) for i in val.split()])
                rule.append(new_val)

        dict_out[rule_num] = rule

    return dict_out


def check_rule(rule_dict, check_string, rule=0, str_idx=0):
    if str_idx == len(check_string):
        return []

    rule = rule_dict[rule]
    if type(rule) is str:
        if check_string[str_idx] == rule:
            return [str_idx+1]
        return []
    else:
        matches = []
        for val in rule:
            sub_matches = [str_idx]

            for sub_rule in val:
                new_matches = []
                for sub_idx in sub_matches:
                    new_matches += check_rule(rule_dict, check_string, sub_rule, sub_idx)
                sub_matches = new_matches

            matches += sub_matches

        return matches


rules_in = data_in[0:132]
test_values = data_in[133:]

#Part 1
print('Part 1:')
rule_dict = create_rules_dict(rules_in)
valid = 0
for i in test_values:
    if len(i) in check_rule(rule_dict, i):
        valid += 1

print(f'Number of valid messages: {valid}')


#Part 2
rule_dict.update({8:[tuple([42]),tuple([42,8])]})
rule_dict.update({11:[tuple([42,31]),tuple([42,11,31])]})
print('\nPart 2:')
valid = 0
for i in test_values:
    if len(i) in check_rule(rule_dict, i):
        valid += 1

print(f'Number of valid messages: {valid}')