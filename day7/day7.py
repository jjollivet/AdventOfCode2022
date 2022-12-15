def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")

    # Part 1 - I started by implementing a tree but ended up changing methods
    # I keep track of the path and path sizes using two lists.
    # Note: this only works assuming we don't enter a same folder twice
    path = []
    path_sizes = []
    current_folder_size = 0
    sum_of_sizes = 0

    max_folder_size = 100000

    # Iterate through all terminal commands
    for instruction in data:
        command = instruction.split(' ')

        # End of list. Work back up to root directory
        if command[0] == '':
            for i in range(len(path)-1):
                if path_sizes[-1] <= max_folder_size:
                    sum_of_sizes += current_folder_size
                    current_folder_size = 0
                path.pop()
                sub_folder_size = path_sizes.pop()
                path_sizes[-1] += sub_folder_size

        # moving up or down the file system
        elif command[1] == 'cd':
            # go up one folder. First, check if folder size < max and add to commulated
            # Then pop folder and add size to parent folder
            if command[2] == '..':
                if path_sizes[-1] <= max_folder_size:
                    sum_of_sizes += path_sizes[-1]
                path.pop()
                sub_folder_size = path_sizes.pop()
                path_sizes[-1] += sub_folder_size

            # go down one folder. append new folder and a size of 0
            else:
                path.append(command[2])
                path_sizes.append(0)

            # Now in a new path - reset folder size to 0
            current_folder_size = 0

        # reading the output of lsx
        else:
            if not (command[0] == 'dir' or command[0] == '$'):
                current_folder_size += int(command[0])
                path_sizes[-1] += int(command[0])

    total_space_used = path_sizes[0]
    print(f'Part 1: Sum of all folders is {total_space_used} and the sum of all folders under 100000 is {sum_of_sizes}')

main()
