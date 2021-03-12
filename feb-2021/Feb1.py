#!/usr/bin/env python3

"""
1st Feb 2021. #516: Medium

This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first 
few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.

"""

"""
Solution: A clever solution requires us to realize that a sevenish number works akin to the binary equivalent of a 
number calculated in powers of 7 instead of 2. Therefore, a binary number 101 (usually 2^2 * 1 + 2^1 * 0 + 2^0 * 1 = 
5) is calculated as 7^2 * 1 + 7^1 * 0 + 7^0 * 1 = 50. This gives us a linear time solution and can be done for any n.

"""

def sevenish(n):
    res = 0
    order = 0

    while n:
        if n & 1:               # if n in binary ends in 1 (is odd)
            res += 7 ** order

        n >>= 1                 # shift n to divide by 2 (next digit in binary form of n)
        order += 1

    return res

def main():
    n = 5
    print(sevenish(n))          # Returns 50 (1, 7, 8, 49, 50)

    return

if __name__ == "__main__":
    main()