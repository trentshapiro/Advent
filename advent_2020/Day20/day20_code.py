import itertools

#read data
current_day = 'day20'
with open(current_day+'_input.txt','r') as f:
    data_in = f.read()

data_in  = data_in.split('Tile ')
data_in = [i for i in data_in if i != '']

class img:
    def __init__(self, label, array):
        self.label = label
        self.array = array
        self.cons = []

    def get_basic_edges(self):
        e_1 = self.array[0]
        e_2 = self.array[-1]
        e_3 = [i[0] for i in self.array]
        e_4 = [i[-1] for i in self.array]
        edges = [e_1,e_2,e_3,e_4]
        return edges

    def get_all_edges(self):
        edges = self.get_basic_edges()
        rev_edges = [list(reversed(i)) for i in edges]
        return edges + rev_edges

img_dict = {}
for i in data_in:
    label, array = i.split(':\n')
    array = array.split('\n')
    array = [[char for char in i] for i in array if i != '']
    img_dict.update({label: img(label, array)})

#all labels
labels = img_dict.keys()
label_pairs = [i for i in list(itertools.combinations(labels, 2)) if i[0] != i[1]]

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

#part 1
answer = 1
for i in labels:
    connections = img_dict[i].cons
    if len(connections) == 2:
        #corner found
        print(i)
        answer *= int(i)
print(answer)