def look_around(x,y, step_count, min_path):
    # increment current position and step
    travelled_grid.add(tuple([x,y]))
    step_count += 1
    # Iterate through all possible directions
    for i in directions:
        test_x = x + i[0]
        test_y = y + i[1]
        # Check if coordinates are valid, and then if they equal end coordinates
        if valid_pos(test_x, test_y, x, y):
            if data[test_x][test_y] == 27 and step_count < min_path:
                min_path = step_count
                step_count -= 1
                travelled_grid.remove(tuple([x,y]))
                return step_count, min_path
            else:
                step_count, min_path = look_around(test_x, test_y, step_count, min_path)
    # Finished all directions, get ready to recurse by removing current position
    step_count -= 1
    travelled_grid.remove(tuple([x,y]))
    return step_count, min_path

# Checks if position is within boundaries of data, if test coord haven't been
# parsed through yet, and if height difference is 0 or 1
def valid_pos(test_x, test_y, cur_x, cur_y):
    if test_x >= 0 and test_y >= 0 and test_x < len(data) and test_y < len(data[0]) and not(tuple([test_x,test_y]) in travelled_grid):
        if data[test_x][test_y] - data[cur_x][cur_y] == 0 or data[test_x][test_y] - data[cur_x][cur_y] == 1:
            return True
    return False


#Import intput file
with open("input.txt") as my_file:
    rawdata = my_file.read().split("\n")
rawdata = list(filter(None, rawdata))

data = []
travelled_grid = set() # used to keep track of path
steps = 0
min_path = 9999999
directions = [[-1,0],[1,0],[0,-1],[0,1]] # 4 possibilities (up, down, left, right)

# re-map chars into numbers such that S=0, a=1, b=2... E=27
for i in range(len(rawdata)):
    data.append([])
    for j in range(len(rawdata[i])):
        if rawdata[i][j] == 'S':
            start_coord = [i,j]
            data[i].append(0)
        elif rawdata[i][j] == 'E':
            end_coord = [i,j]
            data[i].append(27)
        else:
            data[i].append(ord(rawdata[i][j])-ord('a')+1)

steps, min_path = look_around(start_coord[0], start_coord[1], steps, min_path)

print(f'Part 1: {min_path}')
