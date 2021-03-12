#!/usr/bin/env python3

"""
3rd Feb 2021. #518: Easy

This problem was asked by Microsoft.

Given an array of numbers and a number k, determine if there are three entries in the array which add up to the 
specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.

"""

"""
Solution: We could either use three nested loops, or a sorted array that has two pointers. We pick one element and use 
the rest of the list to assign low and high pointers (at i + 1 and len(array) - 1). Now, if the overall sum is k, we 
return true, if the sum is lesser than k, we increase the low pointer and if the sum is greater, we decrease the high 
pointer. This is done for every ith element. 

The solution uses O(n^2) due to the two loops (picking i and picking the other two pointers) and O(1) space as we 
directly use the input array.

"""

def is_summable(arr, k):
    arr.sort()                                      # Sorts the list in ascending order

    for i in range(len(arr) - 1):                   # Pick an initial element
        j = i + 1                                   # Pick a start pointer in the rest of the list (i + 1)
        l = len(arr) - 1                            # Pick an end pointer in the rest of the list at the last element
        while l > j:
            if arr[i] + arr[j] + arr[l] == k:       # If the sum is k, return True
                return True
            elif arr[i] + arr[j] + arr[l] < k:      # If the sum is lesser than k, increment start pointer j
                j += 1
            else:                                   # If the sum is greater than k, decrement end pointer l
                l -= 1
    return False

def main():
    arr = [20, 303, 3, 4, 25]
    k = 49

    print(is_summable(arr, k))                      # Prints True (20 + 4 + 25)

    return

if __name__ == "__main__":
    main()