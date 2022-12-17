import math

def is_interesting_signal(cycle):
    return (cycle - 20) % 40 == 0

def check_sprite_position(cycle_count, sprite_pos, crt_display):
    x_pixel = (cycle_count-1) % 40
    y_pixel = (cycle_count-1) // 40
    if x_pixel == sprite_pos or x_pixel == sprite_pos - 1 or x_pixel == sprite_pos + 1:
        crt_display[y_pixel] = crt_display[y_pixel][:x_pixel] + '#' + crt_display[y_pixel][x_pixel+1:]
    return crt_display

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    data = list(filter(None, data))

    # Part 1
    x_reg = 1
    cycle_count = 0
    signal_str = 0;
    crt_display = []
    for i in range(6):
        crt_display.append('........................................')

    for instruction in data:
        instr = instruction.split()
        # increment regardless of instruction
        cycle_count += 1
        crt_display = check_sprite_position(cycle_count, x_reg, crt_display) # Part 2
        # check whether signal is useful
        if is_interesting_signal(cycle_count):
            signal_str  += cycle_count * x_reg
        # add another cycle if an addx instruction
        if instr[0] == 'addx':
            cycle_count += 1
            crt_display = check_sprite_position(cycle_count, x_reg, crt_display) # Part 2
            if is_interesting_signal(cycle_count): # check whether signal is useful
                signal_str  += cycle_count * x_reg
            x_reg += int(instr[1])

    print(f'Part 1 signal Strenght: {signal_str}')

    print('Part 2:')
    for i in range(len(crt_display)):
        print(crt_display[i])

main()
