def is_interesting_signal(cycle):
    return (cycle - 20) % 40 == 0

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    data = list(filter(None, data))

    # Part 1
    x_reg = 1
    cycle_count = 0
    signal_str = 0;

    for instruction in data:
        instr = instruction.split()
        # increment regardless of instruction
        cycle_count += 1
        # check whether signal is useful
        if is_interesting_signal(cycle_count):
            signal_str  += cycle_count * x_reg
        # add another cycle if an addx instruction
        if instr[0] == 'addx':
            cycle_count += 1
            if is_interesting_signal(cycle_count): # check whether signal is useful
                signal_str  += cycle_count * x_reg
            x_reg += int(instr[1])

    print(f'Part 1 signal Strenght: {signal_str}')

main()
