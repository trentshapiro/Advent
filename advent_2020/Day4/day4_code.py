import yaml
import re

current_day = 'day4'
with open(current_day+'_input.txt','r') as f:
	data_in = f.read()

entries = data_in.split('\n\n')

#yaml doesnt like #
cleaned_entries = [i.replace(' ','\n').replace(':',': ').replace('#','^') for i in entries]

mandatory_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
other_fields = ['cid']


#i dont want to make a check manager please let this not be used in any later question
valid_count = 0
for entry in cleaned_entries:
	entry_dict = yaml.load(entry, Loader=yaml.BaseLoader)

	failed_flag = 0
	for field in mandatory_fields:
		if field not in entry_dict.keys():
			failed_flag = 1
		else:
			value = entry_dict[field]
			if field == 'byr':
				if len(value) != 4 or int(value)>2002 or int(value)<1920:
					failed_flag = 1
					break
			elif field == 'iyr':
				if len(value) != 4 or int(value)>2020 or int(value)<2010:
					failed_flag = 1
					break
			elif field == 'eyr':
				if len(value) != 4 or int(value)>2030 or int(value)<2020:
					failed_flag = 1
					break
			elif field == 'hgt':
				if 'cm' in value:
					if int(value.split('cm')[0])>193 or int(value.split('cm')[0])<150:
						failed_flag = 1
						break
				elif 'in' in value:
					if int(value.split('in')[0])>76 or int(value.split('in')[0])<59:
						failed_flag = 1
						break
				else:
					failed_flag = 1
					break
			elif field == 'hcl':
				value = value.replace('^','#')
				check = re.findall(r'#[0-9a-f]{6}', value)
				if check == [] or check[0] != value:
					failed_flag = 1
					break
			elif field == 'ecl':
				if value not in ['amb','blu','brn','gry','grn','hzl','oth']:
					failed_flag = 1
					break
			elif field == 'pid':
				check = re.findall(r'[0-9]{9}', value)
				if check == [] or check[0] != value:
					failed_flag = 1
					break


	if failed_flag == 0:
		valid_count+=1


print('Total Count: ', len(cleaned_entries))
print('Valid Count: ', valid_count)