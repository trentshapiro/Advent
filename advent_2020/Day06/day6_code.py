current_day = 'day6'
with open(current_day+'_input.txt','r') as f:
	data_in = f.read()

data_in = data_in.split('\n\n')


count_any_yes = 0
count_all_yes = 0
for entry in data_in:
    #part 1
    answers = entry.replace('\n','')
    unique_letters = list(set([char for char in answers]))
    count_any_yes+=len(unique_letters)
    
    #part 2
    num_responses = len(entry.split('\n'))
    for letter in unique_letters:
        if answers.count(letter) == num_responses:
            count_all_yes += 1

print(count_any_yes)
print(count_all_yes)