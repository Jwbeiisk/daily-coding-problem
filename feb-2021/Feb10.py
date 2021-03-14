#!/usr/bin/env python3

"""
10th Feb 2021. #525: Easy

This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

    [[1,  2,  3,  4,  5],
     [6,  7,  8,  9,  10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20]]

You should print out the following:

    1
    2
    3
    4
    5
    10
    15
    20
    19
    18
    17
    16
    11
    6
    7
    8
    9
    14
    13
    12

"""

"""
Solution: We handle each case (left to right, top to bottom, right to left and bottom to top) separately. The starting 
and ending indices are stored to give us a range of numbers not yet printed. This is decreased to make the spiral 
smaller and smaller. This is a very straightforward implementation, and there may be more effective ways of solving 
this problem.

"""

def spiral(arr):    
    row = col = 0                                           # Starting index for a row/column
    row_end = len(arr) - 1                                  # Ending index for a row
    col_end = len(arr[0]) - 1                               # Ending index for a column

    while row < row_end and col < col_end:                  # As long as there are unprinted elements left
        for i in range(col, col_end + 1):                   # Print the first available row (every available column)
            print(arr[row][i])
        row += 1           

        for i in range(row, row_end + 1):                   # Print the last available column (every available row)
            print(arr[i][col_end])
        col_end -= 1

        if row <= row_end:                                  # Checks if there are available rows to be printed
            for i in range(col_end, col - 1, -1):           # Print the last available row (every available column in
                print(arr[row_end][i])                      # reverse)
            row_end -= 1

        if col <= col_end:                                  # Checks if there are available columns to be printed
            for i in range(row_end, row - 1, -1):           # Print the first available column (every available column 
                print(arr[i][col])                          # in reverse)
            col += 1

def main():
    arr1 = [[1,  2,  3,  4,  5],
           [6,  7,  8,  9,  10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20]]

    arr2 = [[1,  2,  3,  4],
            [5,  6,  7,  8],
            [9,  10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20]]

    print("arr1:")
    spiral(arr1)
    print("arr2:")
    spiral(arr2)

    return

if __name__ == "__main__":
    main()