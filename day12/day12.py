# The idea for building a list of all positions at once, rather than the
# recursive function below, is taken from a solution by hyper-neutrino
# This method helps to remove redundancies in travelling to previous unsuccessful paths
def look_around(start_x, start_y):
    list_of_paths = [[start_x, start_y, 0]]

    while len(list_of_paths) != 0:
        cur_x, cur_y, step_count = list_of_paths[0]
        list_of_paths.pop(0)

        # Iterate through all possible directions
        for i in directions:
            test_x = cur_x + i[0]
            test_y = cur_y + i[1]
            if not(valid_pos(test_x, test_y, cur_x, cur_y)):
                continue
            if data[test_x][test_y] == 27: # Exit function when E (27) is reached
                return step_count + 1

            travelled_grid.add(tuple([test_x, test_y]))
            list_of_paths.append([test_x, test_y, step_count + 1])

## previous solution using recursion. However it is the least optimal solution possible
## Kept it here for documentation
# def look_around_recursive(x,y, step_count, min_path):
#     # increment current position and step
#     travelled_grid.add(tuple([x,y]))
#     step_count += 1
#     # Iterate through all possible directions
#     for i in directions:
#         test_x = x + i[0]
#         test_y = y + i[1]
#         # Check if coordinates are valid, and then if they equal end coordinates
#         if valid_pos(test_x, test_y, x, y):
#             if data[test_x][test_y] == 27 and step_count < min_path:
#                 min_path = step_count
#                 step_count -= 1
#                 travelled_grid.remove(tuple([x,y]))
#                 return step_count, min_path
#             else:
#                 step_count, min_path = look_around_recursive(test_x, test_y, step_count, min_path)
#     # Finished all directions, get ready to recurse by removing current position
#     step_count -= 1
#     travelled_grid.remove(tuple([x,y]))
#     return step_count, min_path


# Checks if position is within boundaries of data, if test coord haven't been
# parsed through yet, and if height difference is 0 or 1
def valid_pos(test_x, test_y, cur_x, cur_y):
    if test_x >= 0 and test_y >= 0 and test_x < len(data) and test_y < len(data[0]) and not(tuple([test_x,test_y]) in travelled_grid):
        if data[test_x][test_y] - data[cur_x][cur_y] <= 1:
            return True
    return False


#Import intput file
with open("input.txt") as my_file:
    rawdata = my_file.read().split("\n")
rawdata = list(filter(None, rawdata))

data = []
travelled_grid = set() # used to keep track of path
directions = [[-1,0],[1,0],[0,-1],[0,1]] # 4 possibilities (up, down, left, right)

# re-map chars into numbers such that S=0, a=1, b=2... E=27
for i, row in enumerate(rawdata):
    data.append([])
    for j, val in enumerate(row):
        if val == 'S':
            start_coord = [i,j]
            data[i].append(0)
        elif val == 'E':
            end_coord = [i,j]
            data[i].append(27)
        else:
            data[i].append(ord(val)-ord('a')+1)

print(f'Part 1: {look_around(start_coord[0], start_coord[1])}')
