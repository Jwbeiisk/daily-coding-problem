#!/usr/bin/env python3

"""
3rd Mar 2021. #546: Medium

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements 
to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

    There is 1 smaller element to the right of 3
    There is 1 smaller element to the right of 4
    There are 2 smaller elements to the right of 9
    There is 1 smaller element to the right of 6
    There are no smaller elements to the right of 1

"""

"""
Solution:

"""

def next_smaller(arr):
    new_arr = []

    for i in range(len(arr)):
        # Number of lesser elements to the right
        count = 0

        # For every node to the right of i
        for j in range(i + 1, len(arr)):
            # Increment count if lesser than S[i]
            if arr[i] > arr[j]:
                count += 1
        # Append count for this element to result
        new_arr.append(count)
        
    # Return result
    return new_arr

def main():
    arr = [3, 4, 9, 6, 1]

    print(next_smaller(arr))                # Prints [1, 1, 2, 1, 0]
    
    return

if __name__ == "__main__":
    main()