import numpy as np

move_r = [1, 0]
move_l = [-1,0]
move_u = [0, 1]
move_d = [0,-1]

# Updates the location of a knot depending on direction of travel
# If the knot is at the head, diagonal moves are not possible.
# If it's the tail, then follow the head
def move(current_pos, direction):
    if direction == 'R':
        current_pos = np.add(current_pos,move_r)
    elif direction == 'L':
        current_pos = np.add(current_pos,move_l)
    elif direction == 'U':
        current_pos = np.add(current_pos,move_u)
    elif direction == 'D':
        current_pos = np.add(current_pos,move_d)

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

    # Parse through each instruction
    for instruction in data:
        direction,step = instruction.split()
        # Move the head one step at a time
        for step_size in range(int(step)):
            prev = head
            head = move(head, direction)
            # If distance in either direction > 2, then move the tail
            if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1:
                if head[0] == tail[0] or head[1] == tail[1]:
                    tail = move(tail, direction)
                else:
                    tail = prev
            visited.append(tail)

    unique_loc = set(tuple(i) for i in visited)
    print(f'Part 1: The tail traveled in {len(unique_loc)} unique locations')

    # Part 2
    num_knots = 10
    rope = []
    visited = set()
    movement = [0,0]

    # Create the rope of 10 knots all starting at start location. rope[0] is the head
    for i in range(num_knots):
        rope.append([0,0])
    rope = np.asarray(rope)

    # Parse through each instruction
    for instruction in data:
        direction, step = instruction.split()
        # The code is similar to part 1. Step the head first
        for step_size in range(int(step)):
            rope[0] = move(rope[0], direction)
            # Then iterate through every knot the same way, where head is the previous knot
            for knot in range(1,num_knots):
                # Calculate difference in coordinates
                delta_y = rope[knot-1][1] - rope[knot][1]
                delta_x = rope[knot-1][0] - rope[knot][0]
                # If distance in one direction > 2, then the knot needs to move half of the distance
                if (abs(delta_x) > 1 and delta_y == 0) or (abs(delta_y) > 1 and delta_x == 0):
                    rope[knot] = np.add(rope[knot], [delta_x/2, delta_y/2])
                # If distance in either direction > 2, then the knot needs to move diagonally
                elif abs(delta_x) > 1 or abs(delta_y) > 1:
                    # cap movement to 1 in either direction
                    movement = np.clip([delta_x,delta_y],-1,1)
                    rope[knot] = np.add(rope[knot], movement)

            # Only append the last knot in the rope
            visited.add(tuple(rope[knot]))
            
    print(f'Part 2: The tail traveled to {len(visited)} unique locations')

main()
