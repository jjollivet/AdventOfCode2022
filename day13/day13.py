def find_values(left_value, right_value):
    # First we check if both values are integers
    # If one of the two is, encapsulate the int into a list
    if isinstance(left_value,int):
        # If there are two integers, return difference to check if right > left
        if isinstance(right_value, int):
            return right_value - left_value
        elif isinstance(right_value,list):
            return find_values([left_value], right_value)
    elif isinstance(left_value,list):
        if isinstance(right_value, int):
            return find_values(left_value, [right_value])

    # when both elements are lists, recurse with first element of each
    for i in range(min(len(left_value), len(right_value))):
        # iterate over the minimum length of each. If values are equal, keep going
        if not(left_value[i] is None or right_value[i] is None):
            diff = find_values(left_value[i], right_value[i])
            if diff != 0:
                return diff

    # Last case scenario is when the lengths aren't equal. Return a negative if left > right
    return len(right_value) - len(left_value)

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    data = list(filter(None, data))
    sum_indices = 0

    # Part 1 - I confirmed all of the data is already in list format (and does
    # not contain any nefarious code) so I can use eval to take it as is
    for packet in range(0, int(len(data)),2):
        if find_values(eval(data[packet]),eval(data[packet+1])) > 0:
            sum_indices += (packet/2 + 1)  # Add packet number to sum

    print(f'Part 1 sum of indices: {int(sum_indices)}')

main()
