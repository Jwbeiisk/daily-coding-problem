#!/usr/bin/env python3

"""
22th Feb 2021. #537: Easy

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

    if n is even, the next number in the sequence is n / 2
    if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?

"""

"""
Solution: Spoiler alert: the conjecture is true.

To my understanding, the bonus question is quite hard and I can not imagine it to be anything more than a discussion 
if even asked at an interview. Here is a link though:
https://lucidmanager.org/data-science/project-euler-14/

"""

def is_collatz(n):
    if n == 1:
        return True

    if n % 2 == 0:
        return is_collatz(int(n / 2))
    else:
        return is_collatz(3 * n + 1)

    return False

def main():

    print(is_collatz(49))               # Prints True
    print(is_collatz(82))               # Prints True

    return

if __name__ == "__main__":
    main()