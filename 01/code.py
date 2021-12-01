#!/usr/bin/python3
# Day 01 part 1

import sys

inputfile = open('input.txt', 'r')

input_list = inputfile.read().split('\n')

depth_last = 0
depth_counter = 0

for x in input_list:
    if int(x) > depth_last:
        depth_counter+=1
    depth_last = int(x)

print(depth_counter-1)