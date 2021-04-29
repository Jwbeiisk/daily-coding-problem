#!/usr/bin/env python3

"""
13th Feb 2021. #528: Easy

This problem was asked by Microsoft.

Write a program to determine how many distinct ways there are to create a max heap from a list of N given integers.

For example, if N = 3, and our integers are [1, 2, 3], there are two ways, shown below.

      3      3
     / \    / \
    1   2  2   1

"""

"""
Solution: Followed the well explained, albeit complicated solution at:

https://www.geeksforgeeks.org/number-ways-form-heap-n-distinct-integers/

"""

MAX_N = 105
dp    = [0] * MAX_N
log2  = [0] * MAX_N
nCk   = [[0 for i in range(MAX_N)] for j in range(MAX_N)]

def choose(n, k):
    if k > n:
        return 0
    if n <= 1:
        return 1
    if k == 0:
        return 1

    if nCk[n][k] != -1:
        return nCk[n][k]

    res = choose(n - 1, k - 1) + choose(n - 1, k)
    nCk[n][k] = res
    return res


def get_left(n):
    if n == 1:
        return 0

    h = log2[n]
    n_at_h = 1 << h
    last_at_h = n - (n_at_h - 1)

    if last_at_h >= (n_at_h // 2):
        return n_at_h - 1
    else:
        return n_at_h - 1 - ((n_at_h // 2) - last_at_h)

def nth_heap(n):
    if n <= 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    left = get_left(n)
    res = (choose(n - 1, left) * nth_heap(left)) * nth_heap(n - 1 - left)
    dp[n] = res

    return res

def possible_heaps(arr):
    for i in range(len(arr) + 1):
        dp[i] = -1
        for j in range(len(arr) + 1):
            nCk[i][j] = -1

    curr_log2 = -1
    curr_pow2 = 1

    for i in range(1, len(arr) + 1):
        if curr_pow2 == i:
            curr_log2 += 1
            curr_pow2 *= 2
        log2[i] = curr_log2

    return nth_heap(len(arr))




def main():
    arr = [1, 2, 3]

    print(possible_heaps(arr))

    return

if __name__ == "__main__":
    main()