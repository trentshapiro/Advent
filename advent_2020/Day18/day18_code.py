import ast
import re
from typing import Union

#read data
current_day = 'day18'
with open(current_day+'_input.txt','r') as f:
    data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]


def eval_math(x: int, y: int, op: str) -> int:
    if op == '+':
        return x+y
    elif op == '*':
        return x*y


def clean_eq(eq: str) -> list:
    #replace parenthesis with brackets
    eq = '['+eq.replace('(','[').replace(')',']')+']'
    #replace spaces with commas
    eq = eq.replace(' ',',')
    #surround numbers, +, and * with quotes
    fixed_eq = ''.join(["'"+char+"'" if re.findall(r'[0-9]|\*|\+',char) != [] else char for char in eq])

    #evaluate into list object
    return ast.literal_eval(fixed_eq)


def reduce_eq(eq_in: list, ops: list) -> list:
    #while the output contains any of the operators
    while any(char in eq_in for char in ops):
        #find the index, value of the first operator
        idx = min([eq_in.index(op) for op in ops if op in eq_in])
        op = eq_in[idx]

        #evaluate the math
        reduced_value = eval_math(int(eq_in[idx-1]), int(eq_in[idx+1]), op)

        #reduce the input by replacing math'd numbers and operator with new number
        eq_in = eq_in[0:idx-1]+[reduced_value]+eq_in[idx+2:]

    return eq_in


def eval_eq(eq_in: Union[str, list], ops: list, ordered: bool) -> int:
    #initialize
    current_op = '+'
    current_val = 0

    #if our eq is already a list, leave it, otherwise make list
    eq_list = eq_in if type(eq_in) is list else clean_eq(eq_in)
    
    #for each list element, reduce to int
    reduced_eq = [eval_eq(i, ops, ordered) if type(i) is list else i for i in eq_list]

    # eval, ordered or not
    if ordered:
        for op in ops:
            reduced_eq = reduce_eq(reduced_eq, [op])
    else:
        reduced_eq = reduce_eq(reduced_eq, ops)

    return reduced_eq[0]


#Part 1
print('Part 1: ')
eq_totals = [eval_eq(i, ['*','+'], False) for i in data_in]
print(sum(eq_totals))

#Part 2
print('\nPart 2: ')
eq_totals = [eval_eq(i, ['+','*'], True) for i in data_in]
print(sum(eq_totals))