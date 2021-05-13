#!/usr/bin/env python3

"""
13th Mar 2021. #556: Medium

This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying 
at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array 
non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing 
array.

"""

"""
Solution: The solution is pretty straightforward. We use a flag to count one changed element.

"""

def is_non_decreasing(arr):
    flag = False

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if flag:
                return False

            if i > 0 and arr[i + 1] < arr[i - 1]:
                arr[i + 1] = arr[i]
            else:
                arr[i] = arr[i + 1]

            flag = True 

    return True


def main():
    arr1 = [10, 5, 7]
    arr2 = [10, 5, 1]

    print(is_non_decreasing(arr1))          # Prints True
    print(is_non_decreasing(arr2))          # Prints False
        
    return

if __name__ == "__main__":
    main()