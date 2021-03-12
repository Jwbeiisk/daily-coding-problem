#!/usr/bin/env python3

"""
4th Feb 2021. #519: Medium

This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit 
operations. You can assume b can only be 1 or 0.

"""

"""
Solution: We convert b to a single bit and use basic mathematical operations equivalent to 

(a) b & 1
(b) (x and b) or (y and not b)

"""

def mux(x, y, b):
    b //= 2 ** 28                       # b is now 1 bit (0 or 1) through mathematical left shift
    return (x * b) | (y * (1 - b))      # x * b is x if b is 1, y * not b is y if b is 0

def main():
    x = 0x9f349f3a
    y = 0x24f249bc
    b1 = 0x11111111
    b2 = 0x00000000

    print(mux(x, y, b1))            # Prints x (2671025978)
    print(mux(x, y, b2))            # Prints y (619858364)
    return

if __name__ == "__main__":
    main()