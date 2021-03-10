#!/usr/bin/env python3

"""
14th Jan 2021. BONUS!

Daily Coding Problem skipped an email through some glitch. I've made a sudoku solver instead here.

"""

"""
Solution: We use backtracking to put in a possible value for an empty space and checking if it is a valid field. If true, 
we continue to the next empty space. If no value responds, we backtrack and try a new solution.

"""


def get_empty_cell(sudoku):                         # Returns the indices of an empty cell, None if sudoku is complete
    for r in range(len(sudoku)):
        for c in range(len(sudoku[0])):
            if not sudoku[r][c]:
                return (r, c)
    return None, None


def is_valid(sudoku, row, column, num):             # Checks if the row, column, box  of a cell do not conflict with num
    for i in range(9):
        c = sudoku[i][column] != num
        r = sudoku[row][i] != num

        if not (r and c):                           
            return False                            # Checks row and column (r and c)

    for i in range(3):
        for j in range(3):
            if sudoku[(row - (row % 3)) + i][(column - (column % 3)) + j] == num:
                return False                        # Checks box
    return True


def solve_sudoku(sudoku):                           # Recursively fills in a box without conflict till solved
    r, c = get_empty_cell(sudoku)                   # Indices of next empty cell to be filled
    if r == None:
        return sudoku                               # No more empty cells

    for num in range(1, 10):                        # Potential numbers that can be filled in
        if is_valid(sudoku, r, c, num):             # Number does not conflict at selected cell
            sudoku[r][c] = num                      # Temporarily fill in this cell with potential answer
            if solve_sudoku(sudoku) != None:        # Fill in rest of sudoku with this temporary cell as num
                return sudoku                       # None signals a failed guess, if a grid is returned, it is still a valid guess
            sudoku[r][c] = 0                        # An invalid guess reverts the guesses made to 0 to try again

    return None                                     # Sudoku has no solution


def print_sudoku(sudoku):                           # Prints a fancy grid
    if sudoku == None:
        print("Sudoku has no solution.")
        return

    print("-" * 25)
    for i in range(9):
        for j in range(9):
            if i and not j and i % 3 == 0: print("|", "-" * 21, "|")
            if j % 3 == 0: print("|", end=" ")
            print(sudoku[i][j], end=" ")
        print("|")
    print("-" * 25)

    return


def main():
    sudoku = [[0, 0, 6,  8, 4, 0,  0, 0, 0],        # A valid sudoku
              [2, 0, 1,  0, 6, 0,  0, 0, 7],
              [0, 3, 9,  0, 0, 0,  0, 1, 0],

              [0, 0, 0,  0, 9, 8,  3, 0, 0],
              [0, 6, 0,  0, 0, 0,  0, 9, 0],
              [0, 0, 7,  3, 2, 0,  0, 0, 0],

              [0, 4, 0,  0, 0, 0,  1, 3, 0],
              [7, 0, 0,  0, 1, 0,  8, 0, 4],
              [0, 0, 0,  0, 3, 5,  7, 0, 0]]

    print_sudoku(solve_sudoku(sudoku))

    return


if __name__ == "__main__":
    main()
