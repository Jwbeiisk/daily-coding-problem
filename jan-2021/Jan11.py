#!/usr/bin/env python3

"""
11th Jan 2021. Easy

This problem was asked by Pivotal.

Write an algorithm that finds the total number of set bits in all integers between 1 and N.

"""

"""
Solution: We iterate through every number between 1 and N. For each number, we find the sum of all set bits recursively.
This is done through the integer division operation, which effectively shifts right on the binary value of the integer. 
If the last digit here is 1, the value is odd and we add to the total number of set bits. 

E.g:
for 5: 101, 5 % 2 is 1 (odd)  which means the least significant bit is 1 (total = 1). 5 // 2 = 2: 10 (right shift)
    2: 10,  2 % 2 is 0 (even) which means the least significant bit is 0 (total = 1). 2 // 2 = 1: 1  (right shift)
    1: 1,   1 % 2 is 1 (odd)  which means the least significant bit is 1 (total = 2). 1 // 2 = 0: 0  (right shift)
    0: 0,   loop ends, returns total + 0 = 2

    continue for every number 1 to N
    (count_set_bits(7) = (7 + 6 + 5 + 4 + 3 + 2 + 1) 
                       = 111(3) + 110(2) + 101(2) + 100(1) + 11(2) + 10(1) + 1(1) 
                       = 12)

"""

def count_set_bits(N):
    set_bits = 0
    for i in range(N+1):
        set_bits += integer_set_bits(i)                 # Counts through 0 to N (0 is insignificant) and adds the set bits from each

    return set_bits

def integer_set_bits(n):                                # Recursively finds the number of set bits in the input value
    if n < 1:
        return 0                                        # Does not calculate negative numbers, 0 has no set bits

    if n % 2 == 0:
        return 0 + integer_set_bits(n // 2)             # If the value is even, the least significant bit is not set then right shift

    return 1 + integer_set_bits(n // 2)                 # If the value is odd, the least significant bit is set then right shift

def main():
    N = 7                                               # Should be 12
    print("Total set bits:", count_set_bits(N))

    return

if __name__ == "__main__":
    main()