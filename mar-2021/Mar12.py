#!/usr/bin/env python3

"""
12th Mar 2021. #555: Medium

This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't 
exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

"""

"""
Solution: Binary search.

"""

def element_index(arr, element):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        
        mid = (low+high) // 2
        
        if arr[mid] == element:
            return mid
        
        if arr[low] <= arr[mid]:
            if element >= arr[low] and element < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1                 
        else:
            if element > arr[mid] and element <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return None

def main():
    arr = [13, 18, 25, 2, 8, 10]
    element = 8

    print(element_index(arr, element))          # Prints 4
        
    return

if __name__ == "__main__":
    main()