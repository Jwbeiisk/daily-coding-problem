#!/usr/bin/env python3

"""
30th Jan 2021. #514: Medium

This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its 
length: 4.

Your algorithm should run in O(n) complexity.

"""

"""
Solution: Nothing too fancy. We use hashing to convert a solution that would usually run in O(nlogn) time and O(1) 
space to O(n) time and space. We use a set here, and search for consecutive elements, which is faster than first 
ordering a list and then looping through for sequences.

"""

def longest_sequence(arr):
    count = 0
    s = set(arr)

    for i in range(len(arr)):
        if arr[i] - 1 not in s:
            j = arr[i]
            while j in s:
                j += 1

            count = max(count, j - arr[i])

    return count

def main():
    arr = [100, 4, 200, 1, 3, 2]

    print(longest_sequence(arr))        # Returns 4 (for [1, 2, 3, 4])

    return

if __name__ == "__main__":
    main()
