#!/usr/bin/env python3

"""
15th Feb 2021. #530: Easy

This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and 
substitutions required to change one string to the other. For example, the edit distance between “kitten” and 
“sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

"""

"""
Solution: We use a recursive function that tries all three possible operations to change one word to another, either 
insertion, editing or deletion. The minimum number of all three branches of operations is returned.

"""

def edit_distance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    if l1 == 0:
        return l2
    if l2 == 0:
        return l1

    if s1[l1 - 1] == s2[l2 - 1]:
        return edit_distance(s1[:-1], s2[:-1])

    return 1 + min(edit_distance(s1, s2[:-1]),
                   edit_distance(s1[:-1], s2), 
                   edit_distance(s1[:-1], s2[:-1])
                   )

def main():
    s1 = "kitten"
    s2 = "sitting"

    print(edit_distance(s1, s2))        # Prints 3

    return

if __name__ == "__main__":
    main()