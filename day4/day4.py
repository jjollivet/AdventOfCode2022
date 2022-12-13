import math
import re

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    data = list(filter(None, data))

    num_nested_sections = 0

    # Part 1 - Find thenumber of sections where a set is encompassed within another
    for sections in data:
        section = re.split(',|-', sections)
        section = [eval(i) for i in section]

        if (section[1] >= section[3] and section[0] <= section[2]) or (section[3] >= section[1] and section[2] <= section[0]):
            num_nested_sections += 1

    print(f'Part 1: Number of nested sections: {num_nested_sections}')

main()
