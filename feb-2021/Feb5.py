#!/usr/bin/env python3

"""
5th Feb 2021. #520: Hard

This problem was asked by LinkedIn.

You are given a binary tree in a peculiar string representation. Each node is written in the form (lr), where l 
corresponds to the left child and r corresponds to the right child.

If either l or r is null, it will be represented as a zero. Otherwise, it will be represented by a new (lr) pair.

Here are a few examples:

    A root node with no children: (00)
    A root node with two children: ((00)(00))
    An unbalanced tree with three consecutive left children: ((((00)0)0)0)

Given this representation, determine the depth of the tree.

"""

"""
Solution: Very proud of this solution! We first remove any part of the tree that follows the pattern (00). While that 
node still contributes toward the depth, it's easier to count a level of depth as the brackets that indicate the 
parents are not leaf nodes. Now we calculate the maximum number of either "(" or ")" in a row (not including zeroes). 

In this notation, each consecutive opened bracket indicates the left branch depth and is only punctuated by its own 
closing bracket. Similarly, each closing bracket indicates the right branch depth. The max of these two values is the 
depth.

E.g: "((00)(00))" -> () -> depth 1
     "((((00)0)0)0)" -> (((0)0)0) -> number of consecutive brackets = 3
     This also is true for trees that have alternating unbalanced nodes

"""

import re

def depth(tree):
    d1 = d2 = max_d1 = max_d2 = 0
    tree = re.sub('\(00\)', '', tree)       # Removes all occurrences of "(00)"

    for char in range(len(tree)):           # Iterate through every character in tree
        if tree[char] == ")":               # Reset opened bracket count if closed bracket is encountered
            max_d1 = max(d1, max_d1)        # Only the max count so far is stored
            d1 = 0
        elif tree[char] == "(":             # Increase depth if opened bracket
            d1 += 1

    for char in range(len(tree)):           # Repeat for the other bracket
        if tree[char] == "(":
            max_d2 = max(d2, max_d2)
            d2 = 0
        elif tree[char] == "(":
            d2 += 1

    return max(max_d1, max_d2)              # Highest count for either bracket is the depth

def main():
    t1 = "(00)"
    t2 = "((00)(00))"
    t3 = "((((00)0)0)0)"

    print(t1, depth(t1))            # Prints (00) 0
    print(t2, depth(t2))            # Prints ((00)(00)) 1
    print(t3, depth(t3))            # Prints ((((00)0)0)0) 3

    return

if __name__ == "__main__":
    main()