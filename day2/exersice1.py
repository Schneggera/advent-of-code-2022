#!/usr/bin/env python3

#!/usr/bin/env python3

# file_loc = 'sample1_input.txt'
file_loc = 'input1.txt'

inp_file = open(file_loc)
lines = inp_file.readlines()

# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

# Rock 1
# Paper 2
# Scissor 3

# lose 0
# draw 3
# win 6

total_score = 0

for game in lines:
    shapes = game.split()
    opponent_shape = shapes[0]
    my_shape = shapes[1]

    if my_shape == 'X':
        total_score += 1
    elif my_shape == 'Y':
        total_score += 2
    elif my_shape == 'Z':
        total_score += 3

    if (my_shape == 'X' and opponent_shape == 'C' or
        my_shape == 'Y' and opponent_shape == 'A' or
            my_shape == 'Z' and opponent_shape == 'B'):
        total_score += 6
    elif (my_shape == 'X' and opponent_shape == 'A' or
          my_shape == 'Y' and opponent_shape == 'B' or
          my_shape == 'Z' and opponent_shape == 'C'):
        total_score += 3

print(total_score)