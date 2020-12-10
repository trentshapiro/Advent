current_day = 'day2'
with open(current_day+'_input.txt','r') as f:
	data_in = f.readlines()

data_in = [i.replace('\n','') for i in data_in]
print(len(data_in))

pw_correct = 0
pw_correct_2 = 0
for pw in data_in:
	rule = pw.split(':')[0].replace(' ','-')
	attempt = pw.split(':')[1].replace(' ','')


	rule_min = int(rule.split('-')[0])
	rule_max = int(rule.split('-')[1])
	rule_letter = rule.split('-')[2]

	#part 1
	if rule_min <= attempt.count(rule_letter) <= rule_max:
		pw_correct = pw_correct + 1

	#part 2
	letter_at_lower = attempt[rule_min-1] == rule_letter
	letter_at_upper = attempt[rule_max-1] == rule_letter
	if letter_at_lower != letter_at_upper:
		pw_correct_2 = pw_correct_2 + 1

print(pw_correct)
print(pw_correct_2)
