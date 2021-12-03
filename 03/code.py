#!/usr/bin/python3
# Day 03 part 1

inputfile = open('input.txt', 'r')

input_list = inputfile.read().split('\n')

column_stats = []
column_stats_final = []
column_stats_final_inverse = []
column_stats_halfcount = 0
column_index = 0
line_count = 0

for x in input_list:
    if len(column_stats) == 0:
        column_stats = [ 0 for n in range(len(x)) ]
    #print(x)

    while column_index < len(x):
        if x[column_index] == "1":
            column_stats[column_index] += 1
        #print(column_stats, column_index)
        column_index += 1

    column_index = 0
    line_count += 1

column_stats_halfcount = line_count / 2

column_index = 0
column_stats_final = [ 0 for n in range(len(column_stats))]
column_stats_final_inverse = [ 0 for n in range(len(column_stats))]

while column_index < len(column_stats):
    if column_stats[column_index] >= column_stats_halfcount:
        column_stats_final[column_index] = 1
    else:
        column_stats_final_inverse[column_index] = 1

    column_index += 1

print(column_stats, column_stats_final, column_stats_final_inverse)

column_stats_final_string = "".join(str(y) for y in column_stats_final)
column_stats_final_inverse_string = "".join(str(z) for z in column_stats_final_inverse)

column_stats_final_int = int(column_stats_final_string, 2)
column_stats_final_inverse_int = int(column_stats_final_inverse_string, 2)

print(str(column_stats_final_int), str(column_stats_final_inverse_int)," = ",column_stats_final_int*column_stats_final_inverse_int)