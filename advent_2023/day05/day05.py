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

seeds = [int(i) for i in maps["seeds"][0].split(" ") if i != ""]
maps.pop("seeds")

for k in maps.keys():
    maps[k] = [[int(i) for i in j.split(" ") if j != ""] for j in maps[k]]

# lookup in matrix
def find_map(input_value:int, conv_map:list[list[int]])->int:
    for target_min, input_min, val_range in conv_map:
        if input_value >= input_min and input_value <= input_min + val_range:
            return target_min + (input_value - input_min)
    
    return input_value

locations = seeds
for conv in conv_order[1:]:
    locations = [find_map(i, maps[conv]) for i in locations]

#print(min(locations))

#part 2
def find_map_range(input_value:tuple[int,int], conv_map:list[list[int]]) -> list[tuple[int,int]]:
    valid_min, valid_max = input_value
    source_overlaps = []
    target_overlaps = []

    for target_min, source_min, val_range in conv_map:
        source_max = source_min + val_range - 1

        min_overlap = max(source_min, valid_min)
        max_overlap = min(source_max, valid_max)
        if max_overlap > min_overlap:
            source_overlaps.append((min_overlap,max_overlap))
            min_adj = target_min + (min_overlap - source_min)
            max_adj = target_min + (max_overlap - source_min)
            target_overlaps.append((min_adj,max_adj))
    
    if source_overlaps == []:
        return [(valid_min,valid_max)]

    # fill in any gaps
    source_overlaps = sorted(source_overlaps,key=lambda x:x[0])

    if valid_min < source_overlaps[0][0]:
        source_overlaps = [(valid_min,source_overlaps[0][0]-1)] + source_overlaps
        target_overlaps.append((valid_min,source_overlaps[0][0]-1))

    if valid_max > source_overlaps[-1][1]:
        source_overlaps = source_overlaps + [(source_overlaps[-1][1]+1,valid_max)]
        target_overlaps.append((source_overlaps[-1][1]+1,valid_max))

    list_out = source_overlaps
    for i in range(0,len(source_overlaps)-1):
        if source_overlaps[i][1]+1 != source_overlaps[i+1][0]:
            list_out.append((source_overlaps[i][1]+1,source_overlaps[i+1][0]-1))
            target_overlaps.append((source_overlaps[i][1]+1,source_overlaps[i+1][0]-1))
        
    return target_overlaps

fixed_seeds = [(i,i+j-1) for i,j in zip(seeds,seeds[1:])][::2]
fixed_locations = fixed_seeds

# for i,j in find_map_range((619_902_767,1_268_617_264),maps["seed_to_soil"]):
#     print(f"{i},{j}")

for i in fixed_seeds:
   print(i)
print('\n')
for conv in conv_order[1:]:
    for i in maps[conv]:
       print(i)
    print('\n')
    fixed_locations = [find_map_range(loc,maps[conv]) for loc in fixed_locations]
    fixed_locations = [i for j in fixed_locations for i in j] 
    print(fixed_locations)
    print('\n')

print(min([i for i,_ in fixed_locations]))