#!/usr/bin/env python3

"""
19th Feb 2021. #534: Easy

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily 
should return false, since there's no rearrangement that can form a palindrome.

"""

"""
Solution: Every palindrome has at most one letter that does not repeat, with all other letters in pairs. A single 
letter or a palindrome with an odd length has one single letter [E.g.: 'a' in "a" or 'e' in "racecar"]. One with an 
even length has only letter pairs (E.g.: 'a', 'n' in "anna").

A dictionary is made to store the number of times the letter appears in the word, and barring one exception at most, 
must have an even value for every letter if the word is a palindrome. Time complexity is O(N).

"""

def is_palindrome_anagram(w):
    first_single_letter = False
    letters = {}

    for c in w:
        if c not in letters:
            letters[c] = 0
        letters[c] += 1

    for val in list(letters.values()):    
        if val % 2 != 0:
            if not first_single_letter:
                first_single_letter = True
                continue

            return False 
    return True

def main():
    w1 = "carrace"
    w2 = "daily"

    print(is_palindrome_anagram(w1))        # Prints True
    print(is_palindrome_anagram(w2))        # Prints False

    return

if __name__ == "__main__":
    main()