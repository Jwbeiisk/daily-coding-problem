#!/usr/bin/env python3

"""
6th Jan 2021. Easy

This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.

"""

"""
Solution: Without string functions, we rely on modulus operations to split digits from the number (e.g: 56 mod 10 is 6) 
and integer division to find the order of ten of the number (e.g: 56 // 10 is 5 and 56 // 100 is 0).

Now, we could create a new number from the separated digits by multiplying orders of 10 (e.g: 5*1 + 6*10 = 65). 
However, for larger numbers, we could simply compare the digits at either end and stop as soon as a mismatch is detected.
This means we no longer need to construct the entire reversed number. We strip both ends of the number before 
comparing again in the same way (e.g: in 1221 we first compare the first and last 1's 
then strip it to read 22 and compare the first and last 2's).

"""

def is_palindrome(num):
    if num // 10 == 0 or num // 10 == 1:        #For numbers 0-9 or middle digits in a number with an odd number of digits
        return True

    order = 10
    while (num // order >= 10):
        order *= 10                             # Find the order of the number (10^n)

    while (order > 1):
        l_val = num // order
        r_val = num % 10                        # Gets the rightmost and leftmost digit

        if (l_val != r_val):                    # Compares the said digits
            return False

        num = (num % order) // 10 
        order = order / 100                     # Strips the compared digits for further comparison

    return True

def main():
    
    print(is_palindrome(121), is_palindrome(888), is_palindrome(678))

    return

if __name__ == "__main__":
    main()