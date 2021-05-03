#!/usr/bin/env python3

"""
20th Feb 2021. #535: Medium

This problem was asked by Goldman Sachs.

You are given N identical eggs and access to a building with k floors. Your task is to find the lowest floor that will 
cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks 
when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this 
floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, beginning with the first, until 
we reach the fifth floor, so our solution will be 5.

"""

"""
Solution: https://www.freecodecamp.org/news/how-to-solve-the-google-recruiters-puzzle-about-throwing-eggs-from-a-building-de6e7ef1755d/

"""

def min_trials(N, k):
    # N x k 2D array
    drops = [[0 for i in range(k + 1)] for j in range(N + 1)]
    
    # Number of drops needed if one floor is left is 1, if no floors are left it is 0
    for i in range(N + 1):
        drops[i][0] = 0
        drops[i][1] = 1

    # If only one egg is left, the number of floors left is the number of minimum trials
    for i in range(1, k + 1):
        drops[1][i] = i

    # For every cell after, find drops recursively, adding one each time
    for i in range(2, N + 1):
        for j in range(2, k + 1):
            drops[i][j] = 9999999
            for k in range(j):
                res = 1 + max(drops[i - 1][k - 1], drops[i][j - k])
                # Find least trials due to all the potential splits in floor ranges (see link)
                drops[i][j] = min(drops[i][j], res)

    return drops[N][k]

def main():
    N = 2
    k = 100

    print(min_trials(N, k))         # Prints 14
    print(min_trials(1, 5))         # Prints 5

    return

if __name__ == "__main__":
    main()