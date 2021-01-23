#!/usr/bin/env python3

"""
18th Jan 2021. Easy

This problem was asked by PayPal.

Given a binary tree, determine whether or not it is height-balanced. A height-balanced binary tree can be defined as one in which 
the heights of the two subtrees of any node never differ by more than one.

"""

"""
Solution: We first check if the tree is empty (all empty trees are balanced). Next we recursively check if the subtree is balanced 
on either side of this root. If they both are, we check if the difference between the two sides is greater than 1. Finally, we 
return the height of the root, which is the height of the highest subtree + 1. This makes the function capable of being recursive 
for higher levels of the tree.

E.g: We call the height function on root. This again calls the height function on both left and right child. Each child goes on to 
call the height function until a leaf is reached, which returns 0. Each level above that adds 1 to the height and checks with its 
other branch's value (absent branches are of a height -1). Now if every level is balanced, the tree is determined as balanced.

"""

class Node:
    # Basic binary tree node class
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None
        return


def balanced_height(root):
    # Return false if root is not Node, true if tree is empty
    if type(root) != Node: return -1
    if root.l == None and root.r == None: return 0

    # Checks if left subtree is balanced, returns height of left child or -1 if unbalanced
    l_height = balanced_height(root.l)
    if l_height == -1: return -1

    # Checks if right subtree is balanced, returns height of right child or -1 if unbalanced
    r_height = balanced_height(root.r)
    if r_height == -1: return -1

    # If right and left subtree heights differ by more than 1, return -1
    if abs(r_height - l_height) > 1: return -1

    # Return the highest height recorded in either balanced subtree + 1 for the root's height
    return max(r_height, l_height) + 1


def is_balanced(root):

    # Uncomment this line to also print height of tree
    #print(balanced_height(root))

    # balanced_height calculates height of a balanced tree, returns -1 if unbalanced
    if balanced_height(root) != -1: return True
    return False


def main():

    # Tree 1: Balanced
    #     0
    #    / \
    #   1   2
    #  / \
    # 3   4

    r1 = Node(0)
    p1 = Node(1)
    p2 = Node(2)
    c1 = Node(3)
    c2 = Node(4)

    r1.l = p1
    r1.r = p2
    p1.l = c1
    p1.r = c2


    # Tree 2: Unbalanced
    #     5
    #    / \
    #   6   7
    #  /
    # 8
    #  \
    #   9

    r2 = Node(5)
    p3 = Node(6)
    p4 = Node(7)
    c1 = Node(8)
    g1 = Node(9)

    r2.l = p3
    r2.r = p4
    p3.l = c1
    c1.r = g1

    print("Tree 1:", is_balanced(r1))               # Returns True
    print("Tree 2:", is_balanced(r2))               # Returns False

    return


if __name__ == "__main__":
    main()