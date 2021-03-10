#!/usr/bin/env python3

"""
28th Jan 2021. #512: Medium

This problem was asked by Google.

You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to 
advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can 
get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

"""

"""
Solution: We calculate each step by iterating over each element and calculating the furthest we can go by adding the 
current index to the value stored at that index. If this value were to exceed the length of the array at any point, we 
can return True. If we ever reach an index where the last index still hasn't reached as far, clearly there is no other 
way of reaching that part of the array and we can return False.

"""

def adv(arr):
    last_index = 0

    for i in range(len(arr)):
        if i > last_index:
            break
        last_index = max(last_index, i + arr[i])

    return last_index >= len(arr) - 1


def main():
    arr1 = [1, 3, 1, 2, 0, 1]
    arr2 = [1, 2, 1, 0, 0]

    print(adv(arr1))            # Returns True
    print(adv(arr2))            # Returns False

    return

if __name__ == "__main__":
	main()
