#!/usr/bin/env python3

"""
4th Mar 2021. #547: Hard

This problem was asked by Salesforce.

Given an array of integers, find the maximum XOR of any two elements.

"""

"""
Solution: The easiest approach is brute forcing all pairs, taking O(N^2) time. However, as this is a hard problem, we 
would want to look for a more efficient solution. While there is one that takes O(Nlog(M)) time [M is the largest 
element of the array] using masks, I found a solution using trie to create a linear time answer on HackerRank. This 
solution is explained in depth at 
https://www.ritambhara.in/maximum-xor-value-of-two-elements/

"""

def maxXor(arr):
    ans = 0
    trie = {}
    # Max binary length in array
    N = len(bin(max(arr))) - 2 
    # Array with elements converted to binary
    arr_b = ['{:b}'.format(x).zfill(N) for x in arr]

    # For every element in the array
    for i in range(len(arr_b)):
        node = trie

        # For each binary place value in element, create a key-value pair in trie
        for digit in arr_b[i]:
            node = node.setdefault(digit, {})

        # For every element after arr[i]
        for j in range(i + 1, len(arr_b)):
            node = trie
            xor = ''
            # For each binary place value in arr[j]
            for digit in arr_b[j]:
                # XOR with 1 (NOT)
                tmp = str(int(digit) ^ 1) 
                # At this level, if this trie pattern already exists, follow it
                tmp = tmp if tmp in node else digit 
                # Add this xor value to a string (to get final xor value)
                xor += tmp 
                # Continue to the next place binary digit
                node = node[tmp]
            # Compare the final xor with the maximum value found so far
            ans = max(ans, (int(xor, 2) ^ arr[j]))
    return ans

def main():
    arr = [4, 3, 7, 11]

    print(maxXor(arr))          # Prints 15 (4 ^ 11)
        
    return

if __name__ == "__main__":
    main()