#!/usr/bin/python3
# Day 06 part 1

#import pprint

#pp = pprint.PrettyPrinter(indent=4)

inputfile = open('example.txt', 'r')
input_list = inputfile.read().split('\n')

lanternfish = []

# Initialize
for initial_fish in input_list[0].split(','):
    lanternfish.append(initial_fish)
print("Initial state: ", ",".join(lanternfish))

def run_day(run_lanternfish):
    old_lanternfish = []
    new_lanternfish = []
    counter = 0

    while counter < len(run_lanternfish):
        fish = int(run_lanternfish[counter])
        fish_temp = fish - 1

        if fish_temp < 0:
            new_lanternfish.append(8)
            fish_temp = 6

        old_lanternfish.append(fish_temp)
        counter += 1
        
    return old_lanternfish + new_lanternfish

# Run Days
days_to_run = 256
counter = 1

while counter <= days_to_run:
    lanternfish = run_day(lanternfish)
    #print("After ", counter, " days: ", len(lanternfish))#, lanternfish)
    counter += 1

print("After ", counter - 1, " days: ", len(lanternfish))#, lanternfish)
