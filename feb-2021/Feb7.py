#!/usr/bin/env python3

"""
7th Feb 2021. #522: Medium

This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, 
given the string "abracadabra" and the pattern "abr", you should return [0, 7].

"""

"""
Solution: We iterate through all characters in the string and take subsets matching the length of the pattern to be 
found. If it matches entirely, we append this to the result. 

We need not check the last len(pattern) - 1 number of elements as they are not big enough to contain the pattern, even 
though the code will not throw an error when accessing an index past the string's length.

"""

def find_all(string, pattern):
    res = []
    for i in range(len(string) - len(pattern) + 1):
        if string[i:i + len(pattern)] == pattern:
            res.append(i)

    return res


def main():
    string = "abracadabra"
    pattern = "abr"

    print(find_all(string, pattern))

    return

if __name__ == "__main__":
    main()