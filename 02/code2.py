#!/usr/bin/python3
# Day 02 part 2

inputfile = open('input.txt', 'r')

input_list = inputfile.read().split('\n')

position_horizontal = 0
position_depth = 0
aim = 0

for x in input_list:
    (direction, value) = x.split()
    print("Directions: ",direction, value) 
    if direction == "forward":
        position_horizontal += int(value)
        #print("Horz: ",position_horizontal)
        if aim != 0:
            position_depth += aim * int(value)
            #print("Depth: ",position_depth)
    if direction == "down":
        aim += int(value)
        #print("Down: ",aim)
    if direction == "up":
        aim -= int(value)
        #print("Up: ",aim)
    print("Horiz: ",position_horizontal,", Depth: ",position_depth,", Aim: ",aim)
    print()

print(position_horizontal,position_depth, position_horizontal*position_depth)