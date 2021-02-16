#!/usr/bin/env python3

"""
21st Jan 2021. #505: Easy

This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.

"""

"""
Solution: Array splicing is not an in place method, so we will have to resort to popping and appending values k times.

"""

def rot_k(array, k):                        # Returns an array rotated by k places if possible, else returns None
    if k >= len(array):
        return None

    for i in range(k):
        array.append(array.pop(0))

    return array

def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Array of length 10
    k = 4                                   # To shift 4 places, the new array should start at 5

    print(rot_k(array, k))

    return

if __name__ == "__main__":
    main()
