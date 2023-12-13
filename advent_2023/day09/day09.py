with open("day09_input.txt") as f:
    a = f.readlines()
    a = [i.replace("\n", "") for i in a]

preds = []
for line in a:
    report = [[int(i) for i in line.split(" ")]]

    while not all([i == 0 for i in report[-1]]):
        report.append([j - i for (i, j) in zip(report[-1], report[-1][1:])])

    pred_left, pred_right = 0, 0
    for step in report[::-1]:
        pred_left = step[0] - pred_left
        pred_right = pred_right + step[-1]

    preds.append((pred_left, pred_right))

print([sum(i) for i in zip(*preds)])
