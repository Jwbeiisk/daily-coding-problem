#!/usr/bin/env python3

"""
27th Jan 2021. #511: Medium

This problem was asked by Yelp.

You are given an array of integers, where each element represents the maximum number of steps that can be jumped going 
forward from that element. Write a function to return the minimum number of jumps you must take in order to get from 
the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 
6 to 5, and then from 5 to 9.

"""

"""
Solution: We use a recursive function that calculates the possible jump values for every element encountered. The 
jumps are recorded once the last element is reached and the smallest value is picked. If the element landed on is 0, 
there is no way of proceeding, so this should not be a part of the optimal solution. Since we try every possible route 
here, the time taken is O(N!).

"""

def jumps(arr, jump = 0):
    if arr == [] or len(arr) == 1: return jump
    if arr[0] == 0: return 99999

    moves = [jumps(arr[i:], jump + 1) for i in range(1, min(arr[0] + 1, len(arr)))]
    return min(moves)


def main():
    arr = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]

    print(jumps(arr))       # Returns 2 (6 to 5 and 5 to 9)

    return

if __name__ == "__main__":
	main()
