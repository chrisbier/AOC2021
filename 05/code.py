#!/usr/bin/python3
# Day 05 part 1

#import pprint

#pp = pprint.PrettyPrinter(indent=4)

inputfile = open('input.txt', 'r')
input_list = inputfile.read().split('\n')

class VentField:

    field = {}
    dangerous = 2

    def __init__(self):
        pass
    
    def __repr__(self):
        output = ""
        for x in self.field:
            output_string_temp = "({},{}): {}\n"
            output += output_string_temp.format(x[0], x[1], self.field[x])

        return output

    def add_line(self, start, end):
        start_x = int(start[0])
        start_y = int(start[1])
        end_x = int(end[0])
        end_y = int(end[1])
    
        # Verticle Line
        if start_x == end_x:
            if start_y < end_y:
                y = start_y
                y_end = end_y
            else:
                y = end_y
                y_end = start_y

            while y <= y_end:
                new_value_temp = self.field.setdefault((start_x,y), 0) + 1
                self.field[(start_x,y)] = new_value_temp
                y+=1

        # Horizontal Line
        elif start_y == end_y:
            if start_x < end_x:
                x = start_x
                x_end = end_x
            else:
                x = end_x
                x_end = start_x

            while x <= x_end:
                new_value_temp = self.field.setdefault((x,start_y), 0) + 1
                self.field[(x,start_y)] = new_value_temp
                x+=1
        
        # Diagonal
        else:
            # Get direction
            x = start_x
            y = start_y

            if x < end_x:
                coor1 = 1
                if y < end_y:
                    coor2 = 1
                else:
                    coor2 = -1

            if x > end_x:
                coor1 = -1
                if y < end_y:
                    coor2 = 1
                else:
                    coor2 = -1
            #print(start_x, start_y, coor1, coor2, end_x, end_y)

            while (x, y) != (end_x, end_y):
                new_value_temp = self.field.setdefault((x,y), 0) + 1
                self.field[(x,y)] = new_value_temp

                x += coor1
                y += coor2


    def get_most(self):
        # find most
        most_value = max(self.field, key=self.field.get)
        return self.field[most_value]

    def get_all_most(self):
        # find all most
        #most_value = self.get_most()
        return [ self.field[x] for x in self.field if self.field[x] >= self.dangerous ]


    def get_line(self):
        return [ self.field[(6,4)], self.field[(5,3)], self.field[(4,2)], self.field[(3,1)], self.field[(2,0)] ]


vent_field = VentField()

#vent_field.add_line((1,5), (1,9))
#vent_field.add_line((2,5), (0,5))

# Process
for line in input_list:
    (first_cor, second_cor) = line.split(' -> ')
    first_tup = tuple(first_cor.split(','))
    second_tup = tuple(second_cor.split(','))
    
    vent_field.add_line(first_tup, second_tup)

#print(vent_field)
print("Highest danger point: ", vent_field.get_most())
#print(vent_field.get_line())
all_dangerous = vent_field.get_all_most()
#print(all_dangerous)
print("All Danger points above 2: ", len(all_dangerous))
