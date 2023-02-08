#!/usr/bin/env python3

# file_loc = 'sample1_input.txt'
file_loc = 'input1.txt'

inp_file = open(file_loc)
lines = inp_file.readlines()

highest_num = 0
current_num = 0
for num in lines:
    if num == '\n':
        if current_num > highest_num:
            highest_num = current_num
        current_num = 0
    else:
        current_num += int(num)

print(highest_num)