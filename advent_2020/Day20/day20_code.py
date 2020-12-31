import itertools
from copy import deepcopy

#read data
current_day = 'day20'
with open(current_day+'_input.txt','r') as f:
    data_in = f.read()

data_in  = data_in.split('Tile ')
data_in = [i for i in data_in if i != '']

#class to hold img and metadata
class img:
    '''
    label: img label
    array: matrix of image values, e.g. [['.','#'],['#','#']]
    cons: connected images
    stitched: connected images that are correctly oriented
    final_pos: (x,y) of final position in the overall image
    '''
    def __init__(self, label, array):
        self.label = label
        self.array = array
        self.cons = []
        self.stitched = []
        self.final_pos = None

    def get_basic_edges(self):
        e_1 = self.array[0]
        e_2 = self.array[-1]
        e_3 = [i[0] for i in self.array]
        e_4 = [i[-1] for i in self.array]
        edges = [e_1,e_2,e_3,e_4]
        return edges

    def get_all_edges(self):
        edges = self.get_basic_edges()
        rev_edges = [i[::-1] for i in edges]
        return edges + rev_edges

    def get_edge_dict(self):
        e_1 = self.array[0]
        e_2 = self.array[-1]
        e_3 = [i[0] for i in self.array]
        e_4 = [i[-1] for i in self.array]
        edges = {
            0:e_1, #up
            1:e_3, #left
            2:e_2, #down
            3:e_4  #right
        }
        return edges
    
    def rotate_ccw(self):
        if self.final_pos is not None:
            return self.array
        m = deepcopy(self.array)
        m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
        self.array = m
        return m
    
    def flip_lr(self):
        if self.final_pos is not None:
            return self.array

        m = []
        for i in self.array:
            m.append(i[::-1])
        self.array = m
        return m

#part 1

#load data into dict of images, to reference by labels
img_dict = {}
for i in data_in:
    label, array = i.split(':\n')
    array = array.split('\n')
    array = [[char for char in i] for i in array if i != '']
    img_dict.update({label: img(label, array)})

#list all combinations of imgs to check, only need to check each pair once
labels = img_dict.keys()
label_pairs = [i for i in list(itertools.combinations(labels, 2)) if i[0] != i[1]]

#create list of connections for each img
for pair in label_pairs:
    i_label, j_label = pair

    i_img = img_dict[i_label]
    j_img = img_dict[j_label]
    a = i_img.get_all_edges()
    b = j_img.get_basic_edges()
    matching_edges = sum([i in b for i in a])
    if matching_edges == 1:
        i_cons = i_img.cons
        j_cons = j_img.cons
        if j_label not in i_cons:
            i_cons.append(j_label)
        if i_label not in j_cons:
            j_cons.append(i_label)
        i_img.cons = i_cons
        j_img.cons = j_cons

answer = 1
corners = []
#any img with ony 2 connections is a corner piece
for i in labels:
    if len(img_dict[i].cons) == 2:
        #multiply corner ids for answer
        corners.append(i)
        answer *= int(i)
print('Part 1:')
print(answer)

#part 2
##########################################################
#find starting corner orientation, set to top left corner
##########################################################
start_id = corners[0]
start_img = img_dict[start_id]
match_edges = []

#palatte for final image
final_image = [[0 for i in range(0,12)] for j in range(0,12)]

#find orientation of starting image:
start_img_edges = start_img.get_edge_dict()
start_img_cons = start_img.cons
for edge in start_img_edges.keys():
    edge_value = start_img_edges[edge]

    for con in start_img_cons:
        con_edges = img_dict[con].get_all_edges()
        if edge_value in con_edges:
            match_edges.append(edge)
            break
match_edges = str(sorted(match_edges))

#rotate to be top left based on matched edge pair
rotation_map = {
    '[0, 3]':3,
    '[0, 1]':2,
    '[1, 2]':1,
    '[2, 3]':0
}
rotations = rotation_map[match_edges]
for i in range(0,rotations):
    start_img = start_img.rotate_ccw()

##########################################################
#0 - find label positions in final image, and orient imgs
##########################################################
#set up initial image
start_img.final_pos = (0,0)
img_dict[start_id] = start_img
final_image[0][0] = start_img.label

#define edge mapping for source-target edges given a source-target offset (dx,dy)
source_edge_match_dict = {
    (0 , 1): 3, #right
    (0 ,-1): 1, #left
    (1 , 0): 2, #down
    (-1, 0): 0  #up
}
target_edge_match_dict = {
    (0 , 1): 1,
    (0 ,-1): 3,
    (1 , 0): 0,
    (-1, 0): 2
}

#match images to edges - pos_to_evaluate keeps track of queue of new images to build off of
pos_to_evaluate = [(0,0)]
pos_finished = []
label_finished = []
while pos_to_evaluate != []:
    # initialize left image
    start_x,start_y = pos_to_evaluate[0]
    this_img_id = final_image[start_x][start_y]
    this_img = img_dict[this_img_id]
    this_img_edges = this_img.get_edge_dict()
    imgs_to_match = this_img.cons

    #find list of positions for which there can be a new image
    test_pos = []
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in directions:
        new_x = start_x + i[0]
        new_y = start_y + i[1]
        if new_x >= 0 and new_y >= 0 and new_x <=11 and new_y<=11:
            test_pos.append((new_x,new_y))
    
    # for each positions
    for img_pos in test_pos:
        #if the position is already placed, update stitched for source and target, and skip
        if final_image[img_pos[0]][img_pos[1]] != 0:
            filled_img = img_dict[final_image[img_pos[0]][img_pos[1]]]
            if filled_img.label not in this_img.stitched:
                this_img.stitched = this_img.stitched + [filled_img.label]
                img_dict.update({this_img.label:this_img})
            if this_img.label not in filled_img.stitched:
                filled_img.stitched = filled_img.stitched + [this_img.label]
                img_dict.update({filled_img.label:filled_img})
            continue

        #find the offset of source img to new position, to find which edges to compare
        d_x = img_pos[0] - start_x
        d_y = img_pos[1] - start_y
        source_edge_idx = source_edge_match_dict[(d_x,d_y)]
        source_edge = this_img.get_edge_dict()[source_edge_idx]

        target_edge_idx = target_edge_match_dict[(d_x,d_y)]

        #for each connected image, check for matching edges
        for con_img in imgs_to_match:
            con_img = img_dict[con_img]
            #skip any already stitched images
            if con_img.label in this_img.stitched:
                continue
            else:
                edge_found = False
                
                #rotate ccw, if no matches, flip and repeat
                for i in range(0,4):
                    this_target_edge = con_img.get_edge_dict()[target_edge_idx]
                    if this_target_edge == source_edge:
                        edge_found = True
                        break
                    else:
                        con_img.rotate_ccw()
                if not edge_found:
                    con_img.flip_lr()
                    for i in range(0,4):
                        this_target_edge = con_img.get_edge_dict()[target_edge_idx]
                        if this_target_edge == source_edge:
                            edge_found = True
                            break
                        else:
                            con_img.rotate_ccw()
                #if the edge is found, insert image into final position, update imgs, add new position to evaluation queue
                if edge_found:
                    if con_img.label not in this_img.stitched:
                        this_img.stitched = this_img.stitched + [con_img.label]
                    if this_img.label not in con_img.stitched:
                        con_img.stitched = con_img.stitched + [this_img.label]
                    con_img.final_pos = (img_pos)
                    final_image[img_pos[0]][img_pos[1]] = con_img.label
                    pos_to_evaluate.append(img_pos)
    
    #remove current position from queue
    pos_finished.append(pos_to_evaluate.pop(0))

##########################################################
#1,2,3 - construct full stitched image
##########################################################
cols = []
for idx in range(0,len(final_image)):
    this_col = []
    for i in [j[idx] for j in final_image]:
        this_img = img_dict[i].array
        
        #remove border elements (change to get image number)

        img_trunc = [i[1:][:-1] for i in this_img[1:][:-1]]
        
        for k in img_trunc:
            this_col.append(''.join(k))
    cols.append(this_col)

rough_waters = []
for idx in range(0,len(cols[0])):
    this_row = [i[idx] for i in cols]
    rough_waters.append(''.join(this_row))

#parse final image into img class object (to rotate/flip)
rough_waters = [[char for char in i] for i in rough_waters]
rough_waters = img('waters',rough_waters)

##########################################################
#4- search for dragons
##########################################################
dragon = [
'------------------#-',
'#----##----##----###',
'-#--#--#--#--#--#---'
]

dragon = [[char for char in i] for i in dragon]

def is_dragon(sea, point, dragon):
    x,y = point
    dragon_x_len = len(dragon)
    dragon_y_len = len(dragon[0])

    sub_sea = [i[y:y+dragon_y_len] for i in sea[x:x+dragon_x_len]]
    
    if dragon_x_len != len(sub_sea) or dragon_y_len != len(sub_sea[0]):
        return False

    not_dragon = False
    for i in range(0,dragon_x_len):
        if not_dragon:
            break
        for j in range(0,dragon_y_len):
            if dragon[i][j] == '#' and sub_sea[i][j] != '#':
                not_dragon = True
                break
    
    return not not_dragon

#find sea orientation and dragons - rotate, then flip and repeat
for rot in range(0,4):
    dragons_found = []
    sea = rough_waters.array
    for i in range(0,len(sea)):
        for j in range(0,len(sea[0])):
            if is_dragon(sea, (i,j), dragon):
                dragons_found.append((i,j))
    if len(dragons_found) > 0:
        break
    else:
        rough_waters.array = rough_waters.rotate_ccw()
if len(dragons_found) == 0:
    rough_waters.array = rough_waters.flip_lr()
    for rot in range(0,4):
        dragons_found = []
        sea = rough_waters.array
        for i in range(0,len(sea)):
            for j in range(0,len(sea[0])):
                if is_dragon(sea, (i,j), dragon):
                    dragons_found.append((i,j))
        if len(dragons_found) > 0:
            break
        else:
            rough_waters.array = rough_waters.rotate_ccw()

#assume none of the dragons overlap, pls 
count_dragons = len(dragons_found)
weight_dragon = sum([i.count('#') for i in dragon])
sea_is_dragon = count_dragons * weight_dragon
total_sea = sum([i.count('#') for i in sea])

print('\nPart 2: ')
print(f'total sea #: {total_sea}')
print(f'total dragon #: {sea_is_dragon}')
print(f'total non-dragon sea #: {total_sea - sea_is_dragon}')