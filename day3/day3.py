import math

def point_calculation(common_char):
    if ord(common_char) >= ord('a') and ord(common_char) <= ord('z'):
        points = ord(common_char) - ord('a') + 1
    elif ord(common_char) >= ord('A') and ord(common_char) <= ord('Z'):
        points = ord(common_char) - ord('A') + 27

    return points

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    data = list(filter(None, data))

    sum = 0

    # Part 1 - Find the common character in pairs of strings and sum its numerical value
    for i in data:
        str_len = int(len(i)/2)
        comp1 = set(i[0:str_len])
        comp2 = set(i[str_len:])

        if comp1 & comp2:
            common_char = list(comp1 & comp2)[0]
            points = point_calculation(common_char)

        else: # Not necessary, just in case
            points = 0

        sum += points

    print(f'Part 1: Total points: {sum}')

    # Part 2 - Find the common character in sets of 3 strings and sum their numerical values
    sum = 0

    for i in range(0,len(data),3):
        item1 = set(data[i])
        item2 = set(data[i+1])
        item3 = set(data[i+2])

        if item1 & item2 & item3:
            common_char = list(item1 & item2 & item3)[0]
            points = point_calculation(common_char)

        else: # Not necessary, just in case
            points = 0

        sum += points

    print(f'Part 2: Total points: {sum}')

main()
