#!/usr/bin/env python3

"""
10th Mar 2021. #553: Medium

This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to 
ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is 
lexicographically later as you go down each row. It does not matter whether each row itself is ordered 
lexicographically.

For example, given the following table:

    cba
    daf
    ghi

This is not ordered because of the a in the center. We can remove the second column to make it ordered:

    ca
    df
    gi

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

    abcdef

Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

    zyx
    wvu
    tsr

Your function should return 3, since we would need to remove all the columns to order it.

"""

"""
Solution: Self-explanatory.

"""

def col_del(arr):
    count = 0

    for i in range(len(arr[0])):
        char = 'a'

        for row in arr:
            if ord(row[i]) < ord(char):
                count += 1
                break

            char = row[i]

    return count

def main():
    arr1 = [
        'cba',
        'daf',
        'ghi'
    ]

    arr2 = ['abcdef']

    arr3 = [
        'zyx',
        'wvu',
        'tsr'
    ]

    print(col_del(arr1))        # Prints 1
    print(col_del(arr2))        # Prints 0
    print(col_del(arr3))        # Prints 3
        
    return

if __name__ == "__main__":
    main()