#!/usr/bin/env python3

"""
6th Mar 2021. #549: Hard

This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find 
and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

"""

"""
Solution: With questions with very limited time/space complexities, the solution usually lies in bit wise operations.

In this case, we use a bitwise operation that keeps track of the first two occurrences of a number and cancels it out 
on the third. The only number left at the end of one iteration should be the single one.

To do this, we keep track of the numbers that have appeared 1 modulo 3 times (i.e: 3*n + 1) and numbers that have 
appeared 2 modulo 3 times (i.e: 3*n + 2). We find the bits of elements that appear a third time by getting the common 
'1' bits in ones and twos.

To update ones and twos:

Twos: we add the set bits in both ones and the new element (meaning it has been added to ones already). We have to OR 
the previous value of twos to add it.

Ones: by using XOR on ones and the new element, we get every odd occurrence of the element (we remove the thirds later)

"""

def odd_one_out(arr):
    ones = 0
    twos = 0

    for i in range(len(arr)):
        # Update twos to contain the current  element if already in ones
        twos = twos | (ones & arr[i])
        # Update ones to contain every odd occurrence of an element
        ones = ones ^ arr[i]
        # Find the bits that are set from third occurrences of an element (and NOT to remove it)
        third = ~(ones & twos)

        # Remove the element on its third occurrence
        ones &= third
        twos &= third
    # This leaves the single element as the only odd occurring element
    return ones

def main():
    arr1 = [6, 1, 3, 3, 3, 6, 6]
    arr2 = [13, 19, 13, 13]
        
    print(odd_one_out(arr1))            # Prints 1
    print(odd_one_out(arr2))            # Prints 19

    return

if __name__ == "__main__":
    main()