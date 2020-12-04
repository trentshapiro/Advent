import math 
import numpy as np

current_day = 'day3'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

# pick arbitray big number of times to repeat
min_reps = 1000
ski_map = [[k for k in j] for j in [i*min_reps for i in data_in]]


y_len = len(ski_map)
x_len = len(ski_map[0])

trees_hit = []

for inc in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
	#initialize skiier 
	num_trees = 0
	cur_x = 0
	cur_y = 0
	x_inc = inc[0]
	y_inc = inc[1]
	while cur_y < y_len-1 and cur_x < x_len-1:
		cur_x+=x_inc
		cur_y+=y_inc
		try:
			if ski_map[cur_y][cur_x] == '#':
				num_trees+=1
		except:
			print(cur_x,cur_y)
	print('Slope: ', inc)
	print('Trees: ', num_trees)
	trees_hit.append(num_trees)

print(trees_hit)
print(np.prod(trees_hit))