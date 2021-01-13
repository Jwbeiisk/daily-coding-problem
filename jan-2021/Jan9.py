#!/usr/bin/env python3

"""
9th Jan 2021. Medium

This problem was asked by Facebook.

Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

"""

"""
Solution: Given an array with all positive values, the maximum subarray sum would be the total sum. If they are all negative, 
the maximum subarray sum would be the highest single element. For any other configuration, we group elements split by the negative 
values and find the largest group sum.

"""

def get_subarray_sum(circ_array):                                   # Input circular array and return max subarray sum
    array_sum = []                                                  # Holds all possible positive subarray sums
    cur_sum = 0                                                     # To keep a running total of current subarray
    largest_non_positive = -999999                                  # To find a single element in case of non positive arrays

    for i in range(len(circ_array)):                                # Runs at O(n)
        if circ_array[i] < 0:                                       # If negative, sum up till now is stored and current sum is reset
            array_sum.append(cur_sum)                               # Also compares all negative numbers to find the largest one
            cur_sum = 0                                             
            largest_non_positive = max(largest_non_positive, circ_array[i])
        else:
            cur_sum += circ_array[i]                                # If positive, current value is added to current subarray total

    array_sum[0] += cur_sum                                         # Wrap-around sum (first and last subarray totals)
    max_sum = max(array_sum)                                        # Largest total

    if max_sum == 0:
        return largest_non_positive                                 # In case of only negative numbers
    return max_sum


def main():
    circ_array_1 = [8, -1, 3, 4]
    circ_array_2 = [-4, 5, 1, 0]
    circ_array_3 = [-5, -2, -3, -1, -4]

    print(get_subarray_sum(circ_array_1))                           # Should print 15
    print(get_subarray_sum(circ_array_2))                           # Should print 6
    print(get_subarray_sum(circ_array_3))                           # Should print -1

    return

if __name__ == "__main__":
    main()