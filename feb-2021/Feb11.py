#!/usr/bin/env python3

"""
11th Feb 2021. #526: Easy

This problem was asked by Yahoo.

You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k 
letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of 
moves.

For example, suppose we are given the string daily and k = 1. The best we can create in this case is ailyd.

"""

"""
Solution: Given an unlimited amount of moves, any k greater than 1 would give us a fully sorted string. Therefore, we 
simply sort the string if k > 1. Otherwise, we compare every circular left shifted (by 1) string of the original to 
find the smallest one.

"""

def smallest_lex(string, k):
    if k > 1:
        string_l = [c for c in string]
        string_l.sort()

        return ''.join(string_l)

    elif k == 1:
        smallest_string = string
        for i in range(len(string)):
            tmp = ''.join((string[i:] + string[:i]))    # Shifts the string to the left and appends the first character
            if smallest_string > tmp:
                smallest_string = tmp

        return smallest_string


    
def main():
    string = "daily"
    k = 1

    print(smallest_lex(string, k))                      # Prints "ailyd"

    return

if __name__ == "__main__":
    main()