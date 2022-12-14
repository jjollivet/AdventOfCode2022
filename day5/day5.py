import queue
import re

def print_top_crates(list_of_queues):
    for stack in range(len(list_of_queues)):
        print(list_of_queues[stack].get(), end='')
    print('')

def create_list_of_queues(data):
    # Identify the number and the max height of stacks
    # Note: a look through the puzzle suggest we only have single digit column numbers
    max_stack_height = len(data) - 1
    num_stacks = int(max(data[max_stack_height]))
    list_of_queues = [];

    # I'll be using a LIFO queue for each stack of crates
    # First step is to parse the data and build the queues
    for stack in range(num_stacks):
        q1 = queue.LifoQueue()

        for height in range(max_stack_height):
            crate = data[max_stack_height - height - 1][stack * 4 + 1]

            if crate == ' ':
                break
            else:
                q1.put(crate)

        list_of_queues.append(q1);

    return list_of_queues

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")

    crate_org = data[:data.index('')]

    list_of_queues = create_list_of_queues(crate_org)
    list_of_queues_p2 = create_list_of_queues(crate_org)

    #Define set of instructions
    instructions = list(filter(None, data[data.index('') + 1:]))

    # Find numerical values and perform 'get' and 'put' operations as per each instruction
    for instruction in instructions:
        nums = re.findall('[0-9]+', instruction)
        quantity = int(nums[0])
        from_stack = int(nums[1])
        to_stack = int(nums[2])
        temp_queue = queue.LifoQueue() # Empty queue for part 2

        for i in range(quantity):
            # Part 1
            move_crate = list_of_queues[from_stack-1].get()
            list_of_queues[to_stack-1].put(move_crate)

            # Part 2
            # Re-using principle from part 1 into a temp queue
            move_crate = list_of_queues_p2[from_stack-1].get()
            temp_queue.put(move_crate)

        # Revert order from temp lifo into the second list of queues
        for i in range(quantity):
            move_crate = temp_queue.get()
            list_of_queues_p2[to_stack-1].put(move_crate)

    # get the last crate of each stack
    print_top_crates(list_of_queues)
    print_top_crates(list_of_queues_p2)

main()
