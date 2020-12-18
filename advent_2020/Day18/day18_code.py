import ast
import re

#read data
current_day = 'day18'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def eval_math(x,y,op):
    if op == '+':
        return x+y
    elif op == '*':
        return x*y

def clean_eq(eq_string):
    eq_string = '['+eq_string.replace('(','[').replace(')',']')+']'
    eq_string = eq_string.replace(' ',',')

    fixed_eq = ''
    for char in eq_string:
        if re.findall(r'[0-9]|\*|\+',char) != []:
            fixed_eq+="'"+char+"'"
        else:
            fixed_eq+=char

    return ast.literal_eval(fixed_eq)

def eval_eq_sequential(eq_in):
    current_op = '+'
    current_val = 0
    
    if type(eq_in) is list:
        eq_list = eq_in
    else:
        eq_list = clean_eq(eq_in)
    
    for i in eq_list:
        if type(i) is list:
            new_value = eval_eq_sequential(i)
            current_val = eval_math(current_val, new_value, current_op)
        elif isInt(i):
            new_value = int(i)
            current_val = eval_math(current_val, new_value, current_op)
        elif i in ['*','+']:
            current_op = i
    return current_val

def reduce_by_operater(list_in, op):
    while op in list_in:
        idx = list_in.index(op)
        reduced_value = eval_math(int(list_in[idx-1]), int(list_in[idx+1]), op)
        list_in = list_in[0:idx-1]+[reduced_value]+list_in[idx+2:]
    return list_in

def eval_eq_ordered(eq_in):
    current_op = '+'
    current_val = 0
    
    if type(eq_in) is list:
        eq_list = eq_in
    else:
        eq_list = clean_eq(eq_in)
    
    # reduce parenthesis
    reduced_eq_list = []
    for idx,i in enumerate(eq_list):
        if type(i) is list:
            new_value = eval_eq_ordered(i)
            reduced_eq_list.append(new_value)
        else:
            reduced_eq_list.append(i)

    # eval + first
    reduced_eq_list = reduce_by_operater(reduced_eq_list, '+')
    reduced_eq_list = reduce_by_operater(reduced_eq_list, '*')

    return reduced_eq_list[0]


#Part 1
print('Part 1: ')
eq_totals = [eval_eq_sequential(i) for i in data_in]
print(sum(eq_totals))

#Part 2
print('\nPart 2: ')
eq_totals = [eval_eq_ordered(i) for i in data_in]
print(sum(eq_totals))







