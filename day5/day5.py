import queue
import re

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")

    max_initial_height = 0;
    list_of_queues = [];

    # Identify the number and the max height of stacks
    # Note: a look through the puzzle suggest we only have single digit column numbers
    crate_org = data[:data.index('')]
    max_stack_height = len(crate_org) - 1
    num_stacks = int(max(crate_org[max_stack_height]))

    # I'll be using a LIFO queue for each stack of crates
    # First step is to parse the data and build the queues
    for stack in range(num_stacks):
        q1 = queue.LifoQueue()

        for height in range(max_stack_height):
            crate = crate_org[max_stack_height - height - 1][stack * 4 + 1]

            if crate == ' ':
                break
            else:
                q1.put(crate)

        list_of_queues.append(q1);

    #Define set of instructions
    instructions = list(filter(None, data[data.index('') + 1:]))

    # Find numerical values and perform 'get' and 'put' operations as per each instruction
    for instruction in instructions:
        nums = re.findall('[0-9]+', instruction)
        quantity = int(nums[0])
        from_stack = int(nums[1])
        to_stack = int(nums[2])

        for i in range(quantity):
            move_crate = list_of_queues[from_stack-1].get()
            list_of_queues[to_stack-1].put(move_crate)

    # get the last crate of each stack
    for stack in range(num_stacks):
        print(list_of_queues[stack].get(), end='')

main()
