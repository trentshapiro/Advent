import re

with open("day01_input.txt") as f:
    a = f.readlines()
    a = [i.replace("\n", "") for i in a]

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0
calibrated = 0
for line in a:
    nums = re.findall("[0-9]{1,1}", line)
    first, last = int(nums[0]), int(nums[-1])
    total = total + (first * 10 + last)

    for i, num in enumerate(digits):
        line = line.replace(num, num[0] + str(i + 1) + num[-1])

    nums = re.findall("[0-9]{1,1}", line)
    first, last = int(nums[0]), int(nums[-1])

    calibrated = calibrated + (first * 10 + last)

print(total)
print(calibrated)
