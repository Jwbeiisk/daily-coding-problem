#!/usr/bin/env python3

"""
14th Feb 2021. #529: Hard

This problem was asked by Google.

Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].

"""

"""
Solution: We call a recursive function to take a slice from the string one character at a time. If these are 
palindromes, we save it to a list and continue with the rest of the string. At the same time, we check if the slice 
can be made into a bigger palindrome by continuing to append characters from the string to the slice. When the 
recursive function starts returning values, the smaller list is chosen. This satisfies the condition that a least 
amount of splits should be made.

"""

def is_palindrome(s):
    return s != "" and s == s[::-1]

def palindrome_split(s, substring = "", pal_list = []):
    if not s:
        # Return the list of palindromes once the string is completely iterated recursively
        if not substring:
            return pal_list
        return pal_list + list(substring)

    # Add the next character in the string to the substring
    potential_pal = substring + s[0]
    pal_list1 = []

    # One list adds the substring as is and continues searching for palindromes
    if is_palindrome(potential_pal):
        pal_list1 = palindrome_split(s[1:], pal_list=pal_list + [potential_pal])
    # Another list continues to go through the string's characters to find larger palindromes
    pal_list2 = palindrome_split(s[1:], potential_pal, pal_list)

    # The shorter of the two lists is returned
    return pal_list1 if pal_list1 and len(pal_list1) < len(pal_list2) else pal_list2


def main():
    s1 = "abc"
    s2 = "racecarannakayak"

    print(palindrome_split(s1))     # Prints ['a', 'b', 'c']
    print(palindrome_split(s2))     # Prints ['racecar', 'anna', 'kayak']

    return

if __name__ == "__main__":
    main()