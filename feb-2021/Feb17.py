#!/usr/bin/env python3

"""
17th Feb 2021. #532: Medium

This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that 
have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the 
number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the 
same as (2, 1).

For example, given M = 5 and the list of bishops:

    (0, 0)
    (1, 2)
    (2, 2)
    (4, 0)

The board would look like this:

    [b 0 0 0 0]
    [0 0 b 0 0]
    [0 0 b 0 0]
    [0 0 0 0 0]
    [b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

"""

"""
Solution: The diagonals on a chessboard would have coordinates along a line that has the characteristic of always 
being the same number of steps down as it is across. For example, from (2, 2) to (4, 0) we have to go 2 steps left and 
2 steps down. Thus we simply calculate the number of coordinate pairs where the difference in x or y coordinate values 
is the same (regardless of sign).

"""

def bishop_kills(bishops):
    kills = 0
    for i in range(len(bishops)):
        # Look for every bishop after the selected one
        for j in range(min(i + 1, len(bishops)), len(bishops)):
            if abs(bishops[i][0] - bishops[j][0]) == abs(bishops[i][1] - bishops[j][1]):
                kills += 1
    return kills


def main():
    bishops = [(0, 0),
               (1, 2),
               (2, 2),
               (4, 0)]

    print(bishop_kills(bishops))        # Prints 2

    return

if __name__ == "__main__":
    main()