import math

def main():
    #Import intput file
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    data = list(filter(None, data))

    win = 6
    tie = 3
    opponent_points = 0
    my_points = 0

    # Part 1 - Count points for a rock paper scissors game
    # where A,X = rock. B,Y = paper. C,Z = scissors
    for i in data:
        opponent_move = ord(i[0]) - ord('A') + 1
        my_move = ord(i[2]) - ord('X') + 1

        outcome = (opponent_move - my_move) % 3

        if outcome == 1:
            opponent_points += win
        elif outcome == 0:
            opponent_points += tie
            my_points += tie
        else:
            my_points += win

        my_points += my_move
        opponent_points += opponent_move

    print(f'Part 1: My number of points: {my_points} and the opponent has {opponent_points}')

main()
