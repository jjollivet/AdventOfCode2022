import math

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    data = list(filter(None, data))

    sum = 0

    # Part 1
    for i in data:
        str_len = int(len(i)/2)
        comp1 = set(i[0:str_len])
        comp2 = set(i[str_len:])

        if comp1 & comp2:
            common_char = list(comp1 & comp2)[0]
            points = 0

            if ord(common_char) >= ord('a') and ord(common_char) <= ord('z'):
                points = ord(common_char) - ord('a') + 1
            elif ord(common_char) >= ord('A') and ord(common_char) <= ord('Z'):
                points = ord(common_char) - ord('A') + 27

        else:
            points = 0

        sum += points

    print(f'Part 1: Total points: {sum}')

main()
