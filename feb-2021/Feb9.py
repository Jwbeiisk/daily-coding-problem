#!/usr/bin/env python3

"""
9th Feb 2021. #524: Medium

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 
14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.

"""

"""
Solution: Since we need to achieve this in a single pass, we need to know while iterating through the list whether a 
sum has the potential to become the maximum sum and hence be stored. To do this, we have separate maximums for the 
current range we are summing and the overall highest sum we've achieved so far. This means that a range is discarded 
only when its sum is smaller than the last number iterated alone. Every range is compared to the highest recorded sum, 
which is returned at the end of the loop.

"""

def max_sum(arr):
    max_sum = 0
    tmp_sum = 0

    for num in arr:
        tmp_sum = max(num, tmp_sum + num)       # Current best
        max_sum = max(tmp_sum, max_sum)         # Best recorded so far

    return max_sum

def main():
    array1 = [34, -50, 42, 14, -5, 86]
    array2 = [-5, -1, -8, -9]

    print(max_sum(array1))                      # Prints 137 (42, 14, -5, 86)
    print(max_sum(array2))                      # Prints 0 (taking no elements beats selecting any range)

    return

if __name__ == "__main__":
    main()