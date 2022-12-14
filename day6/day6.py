import queue
import re

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read()

    start_pos = 0
    marker = data[:start_pos+4]

    # Part 1 - Look for rolling set of 4 non-repeated characters
    while(len(set(marker)) < 4):
        start_pos += 1
        marker = data[start_pos:start_pos+4]

    print(start_pos+4)

main()
