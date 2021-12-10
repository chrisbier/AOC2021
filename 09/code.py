#!/usr/bin/python3
# Day 09 part 1

inputfile = open('input.txt', 'r')
input_list = inputfile.read().split('\n')

cave_map = []
low_points = []

# True = test_value is lower than target
# False = test_value is higher than target
def check_value(row, row_mod, column, col_mod, test_value):
    if row + row_mod < 0 or column + col_mod < 0 or row + row_mod > len(cave_map) - 1 or column + col_mod > len(cave_map[0]) - 1:
        return True
    else:
        check_value = int(cave_map[row + row_mod][column + col_mod])
#        if row == 99 and column == 11:
#            print(row + row_mod, column + col_mod)
#            print(row, row_mod, column, col_mod, check_value)

        if check_value <= test_value and check_value != -999:
            return False

    return True


def check_surrounding(row, column):
    # compare each of the 8 directions
    # if there's one lower, return False

    testing_value = int(cave_map[row][column])

    #print("Testing Value: ", testing_value)

    if   not check_value(row, -1, column, -1, testing_value):
        return False
    elif not check_value(row, -1, column,  0, testing_value):
        return False
    elif not check_value(row, -1, column,  1, testing_value):
        return False
    
    elif not check_value(row,  0, column, -1, testing_value):
        return False
    elif not check_value(row,  0, column,  1, testing_value):
        return False

    elif not check_value(row,  1, column, -1, testing_value):
        return False
    elif not check_value(row,  1, column,  0, testing_value):
        return False
    elif not check_value(row,  1, column,  1, testing_value):
        return False

    return True

for line in input_list:
    cave_map.append(line)

#print(cave_map)

cm_index = 0
cm_row = 0

while cm_row < len(cave_map):
    while cm_index < len(cave_map[0]):
        if check_surrounding(cm_row, cm_index):
            #print((cm_row, cm_index), cave_map[cm_row][cm_index])
            low_points.append((cm_row, cm_index))
        cm_index += 1
    cm_row += 1
    cm_index = 0

risk_level = 0

for lp in low_points:
    print(risk_level, "+", int(cave_map[lp[0]][lp[1]]) + 1)
    risk_level += int(cave_map[lp[0]][lp[1]]) + 1

#print(low_points)
print(risk_level)