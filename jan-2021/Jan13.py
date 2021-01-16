#!/usr/bin/env python3

"""
13th Jan 2021. Easy

This problem was asked by WhatsApp.

Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for the 
entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3).

"""

"""
Solution: Compare to a sorted list, find the first element from either end of given list that does not match the sorted list.

"""

def sort_window(array):                             # Takes in array, returns indices of window to be sorted
    unsorted_array = array.copy()
    array.sort()                                    # Unsorted array to be compared with sorted array, flag if l_bound found
    flag = 1

    for i in range(len(array)):                     # Iterate over indices from either end (e.g: array[1] and array[-1])
        if flag and unsorted_array[i] != array[i]:
            l_bound = i                             # Left bound is first element to not match sorted array
            flag = 0

        if unsorted_array[-i] != array[-i] and i != 0:
            r_bound = len(array) - i                # Right bound is last element to not match array
            if not flag:                            # Break if both bounds are found
                break

    if not flag:                                    # If array is unsorted, return bounds
        return (l_bound, r_bound)
    return "Array is sorted in ascending order."    # If array is sorted, return message

def main():
    array = [3, 7, 5, 6, 9]                         # Should return (1, 3)

    print(sort_window(array))

    return

if __name__ == "__main__":
    main()