#!/usr/bin/env python3

"""
8th Feb 2021. #523: Easy

This problem was asked by Jane Street.

Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following 
conditions:

    a + b = M
    a XOR b = N

"""

"""
Solution: Nothing fancy here, we substitute one of (a, b) in the second equation with an equivalent expression from 
the first equation. Here, from a + b = M, we get b = M - a. Now a XOR b = N becomes a XOR (M - a) = N. This way, we 
only look for a single positive number. Further, since a and b may be interchangeable given any solution pair, we only 
have to look in half the potential values lower than M or N.

"""

def num_of_solutions(M, N):
    count = 0
    l = max(M, N)
    mid = l // 2 if l / 2 == 0 else l // 2 + 1

    for a in range(mid):
        b = M - a

        if a ^ b == N:
            count += 1

#           print(a, b)
    return count

def main():
    M = 100
    N = 4

    print(num_of_solutions(M, N))                   # Prints 1 (48, 52)

    return

if __name__ == "__main__":
    main()