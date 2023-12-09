
with open("day09_input.txt") as f:
    a = f.readlines()
    a = [i.replace('\n','') for i in a]


extrapolation_right = 0
extrapolation_left = 0
for line in a:
    report = [[int(i) for i in line.split(" ")]]

    while not all([i==0 for i in report[-1]]):
        report.append([j-i for (i,j) in zip(report[-1],report[-1][1:])])
    
    prediction_left, prediction_right = 0, 0
    for step in report[::-1]:
        prediction_left = step[0] - prediction_left
        prediction_right = prediction_right + step[-1]
    
    extrapolation_left+=prediction_left
    extrapolation_right+=prediction_right

print(extrapolation_right)
print(extrapolation_left)


