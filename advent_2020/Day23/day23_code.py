#read data
current_day = 'day23'
with open(current_day+'_input.txt','r') as f:
    data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]

