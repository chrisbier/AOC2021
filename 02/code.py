#!/usr/bin/python3
# Day 02 part 1

inputfile = open('example.txt', 'r')

input_list = inputfile.read().split('\n')

position_horizontal = 0
position_depth = 0

for x in input_list:
    (direction, value) = x.split()
    if direction == "forward":
        position_horizontal += int(value)
    if direction == "down":
        position_depth += int(value)
    if direction == "up":
        position_depth -= int(value)

print(position_horizontal,position_depth, position_horizontal*position_depth)