#!/usr/bin/env python3

"""
18th Mar 2021. #561: Hard

This problem was asked by Etsy.

Given a sorted array, convert it into a height-balanced binary search tree.

"""

"""
Solution: This is a somewhat textbook explanation, so here's a link that goes in depth enough on BSTs:
https://www.tutorialcup.com/leetcode-solutions/convert-sorted-array-to-binary-search-tree-leetcode-solution.htm

"""

class Node:
    def __init__(self, data=None, l=None, r=None):
        self.data = data
        self.l = l
        self.r = r


def convert_array_to_BST(a, l, r):
    if (l > r):
        return None

    if (l == r):
        return Node(a[l])

    mid = int(l + (r - l) / 2)
    head = Node(a[mid])
    head.l = convert_array_to_BST(a, l, mid - 1)
    head.r = convert_array_to_BST(a, mid + 1, r)

    return head

def sorted_array_to_BST(a):
    return convert_array_to_BST(a, 0, len(a) - 1)

def preorder(head):
    if head == None:
        return

    print(head.data, ' ', end=' ')
    preorder(head.l)
    preorder(head.r)

def main():
    a = [-4 , 0 , 1 , 2 , 7]

    head = sorted_array_to_BST(a)
    preorder(head)

    return

if __name__ == "__main__":
    main()