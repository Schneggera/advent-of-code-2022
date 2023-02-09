#!/usr/bin/env python3

# file_loc = 'sample1_input.txt'
file_loc = 'input1.txt'

inp_file = open(file_loc)
lines = inp_file.readlines()

total_sum = 0

i = 0
while i < len(lines):
    backpack1 = set(lines[i].strip())
    backpack2 = set(lines[i + 1].strip())
    backpack3 = set(lines[i + 2].strip())
    double_items = backpack1 & backpack2 & backpack3
    for item in double_items:
        if item.islower():
            total_sum += ord(item) - 96
        elif item.isupper():
            total_sum += ord(item) - 38
    i += 3

print(total_sum)
