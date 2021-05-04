#!/usr/bin/env python3

"""
23th Feb 2021. #538: Hard

This problem was asked by LinkedIn.

Given a set of characters C and an integer k, a De Bruijn sequence is a cyclic sequence in which every possible 
k-length string of characters in C occurs exactly once.

For example, suppose C = {0, 1} and k = 3. Then our sequence should contain the substrings 
{'000', '001', '010', '011', '100', '101', '110', '111'}, 
and one possible solution would be 00010111.

Create an algorithm that finds a De Bruijn sequence.

"""

"""
Solution: This solution returns more than one sequence. We call recursive functions to make both the substrings of 
length k and the De Bruijn sequences.

First, we make a set of all substrings that chooses a character from C k times.

Second, with this set of substrings, we find a substring that shares all but one character with another substring. 
This gets appended to the final result.

"""

# Finds all substrings of length k with the characters in C
def de_bruijn_substring(C, k, seq=""):
    if not k:
        return set([seq])

    substrings = set()
    for char in C:
        # Recursion runs k times and appends a new character from C each time
        substrings |= de_bruijn_substring(C, k - 1, seq + str(char))

    return substrings

# Constructs De Bruijn sequences from set of substrings
def de_bruijn_sequence(C, k, substrings, seqs, seq=""):
    if not substrings:
        return set([seq])

    for char in C:
        # Choose last k - 1 characters and join with an element in C
        new_substring =seq[1 - k:] + str(char)
        # If this new combination exists in substrings, append to final sequence
        if new_substring in substrings:
            # Find the rest of the sequence through recursion in the same way
            seqs |= de_bruijn_sequence(C, k, substrings - set([new_substring]), seqs, seq + str(char))

    return seqs

# Main function
def de_bruijn(C, k):
    substrings = de_bruijn_substring(C, k)

    # Find a sequence starting with each substring
    seqs = set()
    for substring in substrings:
        seqs |= de_bruijn_sequence(C, k, substrings - set([substring]), seqs, substring)
    
    return substrings, seqs

def main():
    C = [0, 1]
    k = 3

    substrings, sequences = de_bruijn(C, k)

    print("Substrings:", substrings)            # Prints {'001', '010', '110', '100', '101', '000', '111', '011'}
    for s in sequences:
        print(s)                                # E.g: 0001011100

    return

if __name__ == "__main__":
    main()