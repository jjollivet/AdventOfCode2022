def tree_not_counted(tree_heights, index_to_find):
    for i in tree_heights:
        if i == index_to_find:
            return False
    return True

def count_from_treehouse(current_height, tree_heights):
    num_trees = 0
    # Only count trees lower than the tree house height
    # Trees that are taller don't count. Only the first tree of same height counts
    for i in tree_heights:
        if i < current_height:
            num_trees += 1
        else:
            num_trees += 1
            return num_trees
    return num_trees

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

    # All outer trees are visible and must be added
    num_visible_trees = len(index_of_trees) + 2*size_x + 2*size_y -4
    print(f'Part 1: Number of visible trees is {num_visible_trees}')

    # Part 2 - Count trees
    num_visible_trees = 0
    highest_scenic_score = 0

    # Consider only interior trees as scenic score is 0 on outer trees
    for y in range(1,size_y-1):
        for x in range(1,size_x-1):
            temp_scenic_score = 1
            treehouse_height = int(data[y][x])
            # list all trees from a current location to outer border and find its scenic score
            # looking left from treehouse
            tree_heights = []
            for i in range(x-1,-1,-1):
                tree_heights.append(int(data[y][i]))
            temp_scenic_score *= count_from_treehouse(treehouse_height, tree_heights)
            # looking right from treehouse
            tree_heights = []
            for i in range(x+1,size_x,1):
                tree_heights.append(int(data[y][i]))
            temp_scenic_score *= count_from_treehouse(treehouse_height, tree_heights)
            # looking up from treehouse
            tree_heights = []
            for i in range(y-1,-1,-1):
                tree_heights.append(int(data[i][x]))
            temp_scenic_score *= count_from_treehouse(treehouse_height, tree_heights)
            # looking down from treehouse
            tree_heights = []
            for i in range(y+1,size_y,1):
                tree_heights.append(int(data[i][x]))
            temp_scenic_score *= count_from_treehouse(treehouse_height, tree_heights)

            if temp_scenic_score > highest_scenic_score:
                highest_scenic_score = temp_scenic_score

    print(f'Part 2: Highest scenic score is {highest_scenic_score}')
main()
