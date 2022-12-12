import math

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")

    cal = 0
    max_cal = 0

    # Part 1 - Calculate the set of maximum numbers separated by an empty line
    for i in data:
        if i != '':
            cal += int(i)
        elif cal > max_cal:
            max_cal = cal
            cal = 0
        else:
            cal = 0;
    print(f'Part 1: Max is {max_cal}')

main()
