#!/usr/bin/env python3

"""
1st Mar 2021. #544: Hard

This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If 
such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

"""

"""
Solution: 

"""

def sumset(S, k):
    # Return if all values of the list are traversed
    if not S:
        return None
    res = []

    # If the largest value is less than sum, add to total and recurse
    for i in range(1, len(S) + 1):
        if S[-i] <= k:
            res.append(S[-i])

            # Return a list of values adding up to k - current value
            subset = (sumset(S[:-i], k - S[-i]))
            if subset:
                res += subset

            if sum(res) == k:
                return res
            else:
                # No combination with current max value provides k
                res.pop()
    # No combination was found
    return None

def main():
    S = [12, 1, 61, 5, 9, 2]
    k = 24

    print(sumset(sorted(S), k))             # Prints [12, 9, 2, 1]
    
    return

if __name__ == "__main__":
    main()