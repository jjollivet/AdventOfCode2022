def tree_not_counted(list_of_trees, index_to_find):
    for i in list_of_trees:
        if i == index_to_find:
            return False
    return True

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    data = list(filter(None, data))

    size_x = len(data[0])
    size_y = len(data)
    index_of_trees = []

    for y in range(1,size_y-1):
        # Parse from left to right
        max_height = data[y][0]
        for x in range(1,size_x-1):
            index = y * size_y + x
            if data[y][x] > max_height:
                max_height = data[y][x]
                if tree_not_counted(index_of_trees, index):
                    index_of_trees.append(index)

        # Parse from right to left
        max_height = data[y][size_x-1]
        for x in range(size_x-2,0,-1):
            index = y * size_y + x
            if data[y][x] > max_height:
                max_height = data[y][x]
                if tree_not_counted(index_of_trees, index):
                    index_of_trees.append(index)

    for x in range(1,size_x-1):
        # Parse from top to bottom
        max_height = data[0][x]
        for y in range(1,size_y-1):
            index = y * size_y + x
            if data[y][x] > max_height:
                max_height = data[y][x]
                if tree_not_counted(index_of_trees, index):
                    index_of_trees.append(index)
        # Parse from bottom to top
        max_height = data[size_y-1][x]
        for y in range(size_y-2,0,-1):
            index = y * size_y + x
            if data[y][x] > max_height:
                max_height = data[y][x]
                if tree_not_counted(index_of_trees, index):
                    index_of_trees.append(index)

    # include outer trees
    num_visible_trees = len(index_of_trees) + 2*size_x + 2*size_y -4
    print(f'Part 1: Number of visible trees is {num_visible_trees}')
main()
