#!/usr/bin/env python3

"""
17th Mar 2021. #560: Easy

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""

"""
Solution: We make a table containing the number of times each element occurs in the list. This is one pass through the list. Now we compare the number required for an element to sum to k.

"""

def is_summable(arr, k):
    ht = {}

    for i in range(len(arr)):
        if arr[i] not in ht.keys():
            ht[arr[i]] = 1

        else:
            ht[arr[i]] += 1


    for i in range(len(arr)):
        other = k - arr[i]

        is_equal = other == arr[i]
        is_in_table = ht[arr[i]] > 1
        is_other_in_table = other in ht.keys()

        if ((is_equal and is_in_table) or (not is_equal and is_other_in_table)):
            return True

    return False


def main():
    arr = [10, 15, 3, 7]
    k = 17

    print(is_summable(arr, k))          # Prints True (10 + 7 = 17)
        
    return

if __name__ == "__main__":
    main()