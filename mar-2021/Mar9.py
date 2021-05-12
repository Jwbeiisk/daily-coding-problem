#!/usr/bin/env python3

"""
9th Mar 2021. #552: Easy

This problem was asked by Wayfair.

You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

    Dominoes, or 2 x 1 rectangles.
    Trominoes, or L-shapes.

For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

A B B C
A B C C

Given an integer N, determine in how many ways this task is possible.

"""

"""
Solution: https://leetcode.com/problems/domino-and-tromino-tiling/discuss/1150428/Python3-memoization

We can use i and j for each row in the board, and recursively fill up the board, returning 1 if the combination of 
shapes fill the board correctly. We add this up to get the final answer.

For the domino, we increment both i and j by one, for the tromino, we increment one of i and j by one and the other by 
two.

"""

def dp(i, j, N):
    if i == j == N:
        return 1
    if i > N or j > N:
        return 0

    if i == j:
        return dp(i+1, j+1, N) + dp(i+2, j+2, N) + dp(i+1, j+2, N) + dp(i+2, j+1, N)

    elif i > j:
        return dp(i, j+2, N) + dp(i+1, j+2, N)

    else:
        return dp(i+2, j, N) + dp(i+2, j+1, N)

def num_tilings(N):      
    return dp(0, 0, N)

def main():
    N = 4
    print(num_tilings(N))           # Prints 11
        
    return

if __name__ == "__main__":
    main()