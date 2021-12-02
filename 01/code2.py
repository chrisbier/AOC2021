#!/usr/bin/python3
# Day 01 part 2

inputfile = open('input.txt', 'r')

input_list = inputfile.read().split('\n')

depth_last = 0
depth_counter = 0

window_count = round(len(input_list) / 3)
group_start_index = 0
x = 0

while x < window_count:
    try:
        wc1 = int(input_list[x])
        wc2 = int(input_list[x+1])
        wc3 = int(input_list[x+2])
    except:
        print(depth_counter)
        print("quiting")
        exit()

    window_count = wc1 + wc2 + wc3
    #print(wc1, wc2, wc3, "=",window_count)
    print(window_count, depth_last)

    if x == 0:
        depth_last = window_count
        x = 1
    else:
        if window_count > depth_last:
            print(window_count,">",depth_last,"Greater",depth_counter+1)
            depth_counter+=1

        depth_last = window_count
        
        x+=1

print(depth_counter)
