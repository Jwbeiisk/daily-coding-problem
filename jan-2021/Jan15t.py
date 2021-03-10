#!/usr/bin/env python3

"""
15th Jan 2021. Easy

This problem was asked by Palantir.

A typical American-style crossword puzzle grid is an N x N matrix with black and white squares, which obeys the following rules:

Every white square must be part of an "across" word and a "down" word.
No word can be fewer than three letters long.
Every white square must be reachable from every other white square.
The grid is rotationally symmetric (for example, the colors of the top left and bottom right squares must match).
Write a program to determine whether a given matrix qualifies as a crossword grid.

"""

"""
Solution: This is probably the most straighforward approach and there must be (or I choose to believe, at the very least) 
a much more elegant solution. Will update with a better algorithm if I can find one. 
I can see a possible algorithm that picks one white square and attempts to reach every other square while checking the 
3-letter-word-rule. For now, this uninspiring method will have to do.

We first check the symmetry rule by comparing the bottom half of the grid to the reversed strings of the top half. This 
requires only half the rows to be tested (or half + .5 if N is odd). 

Then, we find every 0 (white space) in one half (the other half carries the same result due to symmetry). We now check this 
against the three types of word types across and three types of word shapes down that this white square may belong to. 
These are: [x0x]
           [0xx]
           [xx0] and their transverses (where 0 is the current white square and x is the neighboring white square)

Finally, we check that one white square can reach all the other ones. I did this by making a queue of every white square 
we find attached to a previous one, and increasing a count. This is later compared to the total number of white squares. 
I had to modify the values in the grid to do this, therefore needing to make a copy, which makes me believe even more that 
there must be a prettier solution.

Perhaps the copying parts can be subverted if the functions are called in the following order: is_word, is_symmetric, 
is_reachable. This is because the changes made to the grid won't affect later calculations.

"""

# Takes in the grid and half the rows, returns 1 if symmetric.
def is_symmetric(grid, half_rows):
    # Check every row in top half
    for row in range(half_rows):
        # Copy the list so the reverse isn't reflected in the actual matrix
        cur_row = grid[row].copy()
        # Reverse the list (180 degree rotation)
        cur_row.reverse()
        # The list should match the row of the same distance from the bottom of the grid
        if cur_row != grid[-(row + 1)]:
            # Grid is not symmetric
            return 0
    # Grid is symmetric
    return 1


# Returns 1 (and a message) if all white squares are reachable.
def is_reachable(cw_grid, row, column):
    # Copy grid so changes do not affect the original
    grid = [[i for i in line] for line in cw_grid]
    # Add the first white square found to a queue
    queue = [(row, column)]
    # Number of white squares found so far = 0 (we'll add the first one later)
    count = 0
    # Number of total white squares in grid is found by the following calculation:
    # Number of elements in grid (N x N) minus number of black squares (as they are ones, this is a simple sum of the grid)
    w_count = ((len(grid) * len(grid)) - sum(map(sum, grid)))

    # Stop when we have run this loop for every white square reached through adjacent movement
    while(queue != []):
        # Get a white square's location that we have not evaluated before
        r, c = queue.pop()

        # If a square below exists AND is white
        if r + 1 < len(grid) and not grid[r + 1][c]:
            # Change value of grid so we do not evaluate it again 
            grid[r + 1][c] = 1
            # Add this new square to queue
            queue.append((r + 1, c))
            # Add count of white squares reached
            count += 1

        # If a square above exists AND is white
        if r - 1 >= 0 and not grid[r - 1][c]: 
            # Change value of grid so we do not evaluate it again 
            grid[r - 1][c] = 1
            # Add this new square to queue
            queue.append((r - 1, c))
            # Add count of white squares reached
            count += 1

        # If a square to the right exists AND is white
        if c + 1 < len(grid[0]) and not grid[r][c + 1]: 
            # Change value of grid so we do not evaluate it again 
            grid[r][c + 1] = 1
            # Add this new square to queue
            queue.append((r, c + 1))
            # Add count of white squares reached
            count += 1

        # If a square to the left exists AND is white
        if c - 1 >= 0 and not grid[r][c - 1]:
            # Change value of grid so we do not evaluate it again 
            grid[r][c - 1] = 1 
            # Add this new square to queue
            queue.append((r, c - 1))
            # Add count of white squares reached
            count += 1

    # If every white square is reachable, count is equal to total white square count
    if count == w_count:
        # Grid can be a crossword grid
        return 1, None
    return 0, ("False: Not all white squares are reachable.")



# Returns 1 (and a message) if the selected white square is part of an across word.
def is_word_across(grid, row, column):
    # Shape variables are set if the current white square is a part of said shape
    shape1 = shape2 = shape3 = False

    # [x0x]
    if ( column + 1 < len(grid[0]) ) and ( column - 1 >= 0 ):
        shape1 = (not grid[row][column + 1] and not grid[row][column - 1])

    # [0xx]
    if ( column + 1 < len(grid[0]) ) and ( column + 2 < len(grid[0]) ):
        shape2 = (not grid[row][column + 1] and not grid[row][column + 2])

    # [xx0]
    if ( column - 1 >= 0 ) and ( column - 2 >= 0 ):
        shape3 = (not grid[row][column - 1] and not grid[row][column - 2])

    if shape1 or shape2 or shape3:
        return 1, ("True: Grid is a crossword grid.")
    return 0, ("False: Square at", row + 1, ",", column + 1, "is not a word, hence not a crossword grid.")


# Returns 1 (and a message) if the selected white square is part of a down word.
def is_word_down(grid, row, column):
    # Shape variables are set if the current white square is a part of said shape
    shape1 = shape2 = shape3 = False

    # [x0x]T (transverse)
    if ( row + 1 < len(grid) ) and ( row - 1 >= 0 ):
        shape1 = (not grid[row + 1][column] and not grid[row - 1][column])

    # [0xx]T
    if ( row + 1 < len(grid) ) and ( row + 2 < len(grid) ):
        shape2 = (not grid[row + 1][column] and not grid[row + 2][column])

    # [xx0]T
    if ( row - 1 >= 0 ) and ( row - 2 >= 0 ):
        shape3 = (not grid[row - 1][column] and not grid[row - 2][column])

    if shape1 or shape2 or shape3:
        return 1, ("True: Grid is a crossword grid.")
    return 0, ("False: Square at", row + 1, ",", column + 1, "is not a word, hence not a crossword grid.")

# Checks if the white square is part of a word either across or down, returns a flag and message.
def is_word(grid, row, column):
    down, msg1 = is_word_down(grid, row, column)
    across, msg2 = is_word_across(grid, row, column)

    # Returns either fail message if it exists (favors across)
    return (down, msg1) if across else (across, msg2)


# Returns a message on whether the grid is a crossword grid and where it deviates from one, if at all.
def is_crossword_grid(grid):
    # Flag is set if grid is a crossword grid
    flag = 0
    # A crossword grid is symmetric, so check only half the rows (including middle if N is odd)
    half_rows = (len(grid) // 2) if (len(grid) % 2 == 0) else ((len(grid) // 2) + 1)

    # Stops further checking if not symmetric
    if not is_symmetric(grid, half_rows) or (len(grid) != len(grid[0])):
        return "False: Grid is not symmetric, hence not a crossword grid."

    # For each white square
    for row in range(half_rows):
        for column in range(len(grid[row])):
            if not grid[row][column]:
                # Runs only for first white square
                if not flag:
                    flag, msg = is_reachable(grid, row, column)
                    # Stops further checking if white squares are not reachable
                    if not flag:
                        break
                
                # Checks if each square is part of a three letter word, down or across 
                flag, msg = is_word(grid, row, column)
                # Stops further checking if not a word
                if not flag:
                    return msg

    # Returns a string
    return msg 


def main():
    cw_grid1 = [[1, 1, 1, 0, 0, 0, 1],              # A crossword grid (returns True)
                [1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 1, 1, 1]]

    cw_grid2 = [[1, 1, 1, 0, 1, 0, 1],              # Not a crossword grid (returns False)
                [1, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 1, 1]]

    print("cw_grid1 -", is_crossword_grid(cw_grid1))
    print("cw_grid2 -", is_crossword_grid(cw_grid2))

    return


if __name__ == "__main__":
    main()
