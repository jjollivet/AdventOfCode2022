import numpy as np

move_r = [1, 0]
move_l = [-1,0]
move_u = [0, 1]
move_d = [0,-1]

# Updates the location of a knot depending on direction of travel
# If the knot is at the head, diagonal moves are not possible.
# If it's the tail, then follow the head
def move(current_pos, head, direction, diagonal_move_possible):
    if direction == 'R':
        current_pos = np.add(current_pos,move_r)
        if diagonal_move_possible and not(head[1] == current_pos[1]):
            current_pos[1] = head[1]
    elif direction == 'L':
        current_pos = np.add(current_pos,move_l)
        if diagonal_move_possible and not(head[1] == current_pos[1]):
            current_pos[1] = head[1]
    elif direction == 'U':
        current_pos = np.add(current_pos,move_u)
        if diagonal_move_possible and not(head[0] == current_pos[0]):
            current_pos[0] = head[0]
    elif direction == 'D':
        current_pos = np.add(current_pos,move_d)
        if diagonal_move_possible and not(head[0] == current_pos[0]):
            current_pos[0] = head[0]

    return current_pos

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    data = list(filter(None, data))

    # Part 1
    head = [0,0]
    tail = [0,0]
    visited = []

    for instruction in data:
        direction,step = instruction.split()

        for step_size in range(int(step)):
            head = move(head, [0,0], direction, False)
            #print(f'H:{head}')
            if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1:
                tail = move(tail, head, direction, True)
                #print(f'T:{tail}')
            visited.append(tail)

    unique_loc = set(tuple(i) for i in visited)
    print(f'Part 1: The tail traveled in {len(unique_loc)} unique locations')

main()
