#!/usr/bin/env python3

"""
26th Feb 2021. #541: Easy

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated 
successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as 
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely 
of alphabetic characters. You can assume the string to be decoded is valid.

"""

"""
Solution: Two while loops that run over both the dissimilar characters and the similar ones. The inner loop also 
counts the number of repeated characters.

"""

def run_length_decoding(s):
    res = ""
    i = 0

    while i < len(s):
        freq = 1
        while(i + 1 < len(s) and s[i + 1] == s[i]):
            freq += 1
            i += 1
        res += str(freq) + s[i]
        i += 1
    return res

def main():
    s = "AAAABBBCCDAA"

    print(run_length_decoding(s))
    
    return

if __name__ == "__main__":
    main()