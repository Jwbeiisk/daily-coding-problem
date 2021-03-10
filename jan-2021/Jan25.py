#!/usr/bin/env python3

"""
25th Jan 2021. #509: Medium

This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

"""

"""
Solution: We compare the ends of the word and insert the first letters to the last and vice versa. Each of these is continued recursively until we reach two alternative ways of inserting these letters at each step. One of the two is chosen at every recursive step based on either length or alphabetical order.

"""

def make_palindrome(s):
    if s == s[::-1]:
        return s

    if s == s[-1]:
        return s[0] + make_palindrome(s[1:-1]) + s[-1]
    else:
        front = s[0] + make_palindrome(s[1:]) + s[0]
        end = s[-1] + make_palindrome(s[:-1]) + s[-1]

        if len(front) < len(end):
            return front
        elif len(front) > len(end):
            return end
        return front if front < end else end

def main():
    test1 = "race"
    test2 = "google"

    print(make_palindrome(test1))   # Outputs "ecarace"
    print(make_palindrome(test2))   # Outputs "elgoogle"

    return

if __name__ == "__main__":
	main()
