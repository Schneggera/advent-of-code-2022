#!/usr/bin/env python3

# file_loc = 'sample1_input.txt'
file_loc = 'input1.txt'

inp_file = open(file_loc)
lines = inp_file.readlines()

total_sum = 0

for backpack in lines:
    backpack = backpack.strip()
    item_number = len(backpack)
    middle = int(item_number/2)
    comp1 = set(backpack[0:middle])
    comp2 = set(backpack[middle:item_number])
    double_items = comp1 & comp2
    for item in double_items:
        if item.islower():
            total_sum += ord(item) - 96
        elif item.isupper():
            total_sum += ord(item) - 38

print(total_sum)
