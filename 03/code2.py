#!/usr/bin/python3
# Day 03 part 2

#from bitarray import bitarray
import math

inputfile = open('input.txt', 'r')

input_list = inputfile.read().split('\n')

# Processing 2
oxy_gen = [ x for x in input_list ]
co2_scrub = [ x for x in input_list ]
column_index = 0

def get_most_common(my_list, column_spot):
    list_len = len(my_list)
    spot_count = 0

    for x in my_list:
        if x[column_spot] == "1":
            spot_count += 1
    #print(spot_count, math.ceil(list_len / 2))
    
    if spot_count >= math.ceil(list_len / 2):
        #print("returning", 1)
        return 1
    else:
        return 0

def get_least_common(my_list, column_spot):
    list_len = len(my_list)
    spot_count = 0

    for x in my_list:
        if x[column_spot] == "1":
            spot_count += 1
    #print(spot_count, math.ceil(list_len / 2))
    
    if spot_count >= math.ceil(list_len / 2):
        return 0
    else:
        return 1

def del_column(my_list, column_spot, target_value):
    new_list = []

    for x in my_list:
        if x[column_spot] != str(target_value):
            new_list.append(x)
    return new_list

def find_next_value(my_list, my_column_index):
    #print(len(my_list), my_column_index)
    most_common = get_most_common(my_list, my_column_index)
    if most_common == 1:
        my_common = 0
    else:
        my_common = 1
    new_list = del_column(my_list, my_column_index, my_common)

    #print(new_list)

    if len(new_list) == 1:
        return new_list
    return find_next_value(new_list, my_column_index + 1)

def find_next_value_least(my_list, my_column_index):
    #print(len(my_list), my_column_index)
    least_common = get_least_common(my_list, my_column_index)
    if least_common == 1:
        my_common = 0
    else:
        my_common = 1
    new_list = del_column(my_list, my_column_index, my_common)

    #print(new_list)

    if len(new_list) == 1:
        return new_list
    return find_next_value_least(new_list, my_column_index + 1)
    
#print(del_column(oxy_gen, 0, 0))
#counterasdf = 0
#while counterasdf <= len(oxy_gen[0]):
#    print("most common: ",get_most_common(oxy_gen, counterasdf))
#    counterasdf += 1
found_oxy_gen = find_next_value(oxy_gen, 0)
print(found_oxy_gen)
decimal_number = int("".join(str(y) for y in found_oxy_gen), 2)
print(decimal_number)

found_co2_scrub = find_next_value_least(co2_scrub, 0)
print(found_co2_scrub)
decimal_number_least = int("".join(str(y) for y in found_co2_scrub), 2)
print(decimal_number_least)

print("Final: ", decimal_number * decimal_number_least)