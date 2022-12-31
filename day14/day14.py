import re

#Import intput file
with open("input.txt") as my_file:
    data = my_file.read().split("\n")
    data = list(filter(None, data))

# Start by logging all cave walls into a set
walls = set()
bottom = 0
for line in data:
    values = re.findall('\d+', line)
    for i in range(int(len(values)/2)-1):
        start_x = int(values[i*2])
        end_x = int(values[i*2+2])
        start_y = int(values[i*2+1])
        end_y = int(values[i*2+3])
        if start_x == end_x:
            for wall in range(min(start_y, end_y), max(start_y, end_y) + 1):
                walls.add(tuple([start_x, wall]))
        if start_y == end_y:
            for wall in range(min(start_x, end_x), max(start_x, end_x) + 1):
                walls.add(tuple([wall, start_y]))
        # Find bottom
        bottom = max(bottom, start_y, end_y)

# Part 1 - Simulate until the
# Location of all sand units
sand_pile = set()
num_sand_units = 0
bottom_reached = False

# Iterate for each unit of sand
while not(bottom_reached):
    sand_unit = [500,0]
    unit_deposited = False

    # Iterate for each movement of each unit of sand
    while not(unit_deposited):
        occupied = sand_pile.union(walls)
        # First check space directly under
        if tuple([sand_unit[0], sand_unit[1] + 1]) not in occupied:
            sand_unit[1] += 1
        # Then check for space one under and one left
        elif tuple([sand_unit[0] - 1, sand_unit[1] + 1]) not in occupied:
            sand_unit[0] -= 1
            sand_unit[1] += 1
        # Then check for space one under and one right
        elif tuple([sand_unit[0] + 1, sand_unit[1] + 1]) not in occupied:
            sand_unit[0] += 1
            sand_unit[1] += 1
        else: # Otherwise the unit of sand settles
            sand_pile.add(tuple(sand_unit))
            unit_deposited = True
            num_sand_units += 1
        # Check if sand reached below the bottom most walls
        if sand_unit[1] > bottom:
            unit_deposited = True
            bottom_reached = True

print(f'Part 1: Num of sand units is {num_sand_units}')
