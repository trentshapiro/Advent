current_day = 'day1'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [int(i.replace('\n','')) for i in data_in]

for i in data_in:
	for j in data_in:
		for k in data_in:
			if i + j + k == 2020:
				print(i)
				print(j)
				print(k)
				print(i*j*k)