#!/usr/bin/env python3

"""
4th Jan 2021. Easy

This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

"""

"""
Solution: Create a set from the list, i.e. remove any repetitions.
Without the inbuilt function, use either a dictionary to check if the element exists already 
or manually check (if x in new_list) for smaller lists.

"""

def make_subarray(array):
    return len(set(array))                          # Removes duplicates

def main():

    print(make_subarray([5, 1, 3, 5, 2, 3, 4, 1]))
    
    return

if __name__ == "__main__":
    main()