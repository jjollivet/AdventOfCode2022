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

    # Part 2 - Calculate sum of top three sets of numbers separated by an empty line
    cal = 0
    total_cal = []

    for i in data:
        if i != '':
            cal += int(i)
        else:
            total_cal.append(cal)
            cal = 0

    total_cal.sort(reverse=True)
    print(f'Sum of top three is {total_cal[0]+total_cal[1]+total_cal[2]}')

main()
