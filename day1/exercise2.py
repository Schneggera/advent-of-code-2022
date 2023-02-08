#!/usr/bin/env python3

# file_loc = 'sample1_input.txt'
file_loc = 'input1.txt'

inp_file = open(file_loc)
lines = inp_file.readlines()

num_list = []
current_num = 0
for num in lines:
    if num == '\n':
        num_list.append(current_num)
        current_num = 0
    else:
        current_num += int(num)

num_list.sort(reverse=True)
num_top_three = num_list[0] + num_list[1] + num_list[2]
print(num_top_three)