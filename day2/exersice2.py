#!/usr/bin/env python3

# file_loc = 'sample1_input.txt'
file_loc = 'input1.txt'

inp_file = open(file_loc)
lines = inp_file.readlines()

# A = Rock
# B = Paper
# C = Scissors

# X = lose
# Y = draw
# Z = win

# Rock 1
# Paper 2
# Scissor 3

# lose 0
# draw 3
# win 6

total_score = 0

def toWin(input):
    if input == 'A':
        return 2
    elif input == 'B':
        return 3
    elif input == 'C':
        return 1

def toDraw(input):
    if input == 'A':
        return 1
    elif input == 'B':
        return 2
    elif input == 'C':
        return 3

def toLose(input):
    if input == 'A':
        return 3
    elif input == 'B':
        return 1
    elif input == 'C':
        return 2


for game in lines:
    shapes = game.split()
    opponent_shape = shapes[0]
    game_result = shapes[1]

    if game_result == 'Z':
        total_score += 6
        total_score += toWin(opponent_shape)
    elif game_result == 'Y':
        total_score += 3
        total_score += toDraw(opponent_shape)
    elif game_result == 'X':
        total_score += toLose(opponent_shape)
print(total_score)
