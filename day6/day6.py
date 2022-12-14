import queue
import re

def start_of_packet(data, num_char):
    start_pos = 0;
    marker = data[:start_pos+num_char]

    while(len(set(marker)) < num_char):
        start_pos += 1
        marker = data[start_pos:start_pos+num_char]

    return start_pos + num_char

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read()

    print(f'Part 1 start-of-packet char: {start_of_packet(data, 4)}')
    print(f'Part 2 start-of-packet char: {start_of_packet(data, 14)}')

main()
