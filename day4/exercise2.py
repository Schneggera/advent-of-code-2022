#!/usr/bin/env python3

# file_loc = 'sample1_input.txt'
file_loc = 'input1.txt'

inp_file = open(file_loc)
lines = inp_file.readlines()

count_overlap = 0

for line in lines:
    pair = line.strip().split(',')
    elf1 = pair[0].split('-')
    elf2 = pair[1].split('-')
    elf1_range = list(range(int(elf1[0]), int(elf1[1])+1))
    elf2_range = list(range(int(elf2[0]), int(elf2[1])+1))
    overlap = [ e1 for e1 in elf1_range if e1 in elf2_range ]

    if len(overlap) > 0:
        count_overlap += 1

print(count_overlap)