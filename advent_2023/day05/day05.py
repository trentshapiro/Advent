from collections import Counter
from math import floor


input_type = "input"
maps = {}


conv_order = [
    "seeds",
    "seed_to_soil", 
    "soil_to_fert", 
    "fert_to_wat", 
    "wat_to_light",
    "light_to_temp", 
    "temp_to_humi", 
    "humi_to_loc", 
]

# read input, format matrices
for file in conv_order:    
    with open(f"{input_type}/{file}.txt") as f:
        maps[file] = [i.replace('\n','') for i in f.readlines()]

seeds = sorted([int(i) for i in maps["seeds"][0].split(" ") if i != ""])
maps.pop("seeds")

for k in maps.keys():
    maps[k] = [[int(i) for i in j.split(" ") if j != ""] for j in maps[k]]

# lookup in matrix
def find_map(input_value, conv_map):
    for target_min, input_min, val_range in conv_map:
        if input_value >= input_min and input_value <= input_min + val_range:
            return target_min + (input_value - input_min)
    
    return input_value

locations = seeds
for conv in conv_order[1:]:
    locations = [find_map(i, maps[conv]) for i in locations]

print(min(locations))