import itertools

#read data
current_day = 'day21'
with open(current_day+'_input.txt','r') as f:
    data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

class recipe:
    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens

recipes = []
for i in data_in:
    ingredients = i.split(' (')[0]
    ingredients = ingredients.split(' ')

    allergens = i.split('(contains ')[-1].replace(')','')
    allergens = allergens.split(', ')

    recipes.append(recipe(ingredients, allergens))


#individual allergens
allergens_list = list(set([j for i in recipes for j in i.allergens]))

#ingredients that could be allergens
allergen_possibilities = {}
for check_allergen in allergens_list:
    possible_ingredients = []
    
    for recipe in recipes:
        if check_allergen in recipe.allergens:
            possible_ingredients.append(recipe.ingredients)
    
    uniq_ingredients = list(set([j for i in possible_ingredients for j in i]))
    
    possible_allergens = []
    for ing in uniq_ingredients:
        if all(ing in i for i in possible_ingredients):
            possible_allergens.append(ing)
    allergen_possibilities.update({check_allergen:possible_allergens})

#ingredients not in list of possible allergens
ingredients_list = list(set([j for i in recipes for j in i.ingredients]))
possible_allergens_list = list(set([j for i in allergen_possibilities.values() for j in i]))
not_possible_allergens_list = [i for i in ingredients_list if i not in possible_allergens_list]

count_not_possible = 0
for ing in not_possible_allergens_list:
    for i in recipes:
        if ing in i.ingredients:
            count_not_possible+=i.ingredients.count(ing)


print('Part 1: ')
print(f'Instances of not allergen ingredients: {count_not_possible}')

def dict_remove_subval(dict_in, remove_val):
    dict_out = {}
    for i in dict_in.keys():
        value = dict_in[i]
        new_value = [j for j in value if j != remove_val]
        dict_out.update({i:new_value})
    return dict_out

final_allergens = {}
while len(final_allergens.keys()) < len(allergens_list):
    for i in allergens_list:
        if len(allergen_possibilities[i]) == 1:
            final_allergens.update({i:allergen_possibilities[i][0]})
            allergen_possibilities = dict_remove_subval(allergen_possibilities, allergen_possibilities[i][0])

out_list = ','.join([final_allergens[i] for i in sorted(allergens_list)])
print('\nPart 2:')
print(f'Final allergen list: {out_list}')