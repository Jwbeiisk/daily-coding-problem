#!/usr/bin/env python3

"""
25th Feb 2021. #540: Easy

This problem was asked by Morgan Stanley.

In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to 
left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

           1
        /     \
      2         3
     / \       / \
    4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].

"""

"""
Solution: Recursive inorder traversal, but while keeping track of the height of the current node (and whether it is 
even or odd).

"""


# Binary Tree Node
class Node:
    def __init__(self, data, l_child=None, r_child=None):
        self.data = data
        self.l = l_child
        self.r = r_child
        return

    def __repr__(self):
        return str(self.data)


# Recursively traverses inorder
def boustrophedon_util(root, levels, height=0):
    # Height of root's children
    height += 1
    # True if this height an odd layer
    is_odd = height % 2
    node_at_level = []

    # Appends left child if any and recurses that branch
    if root.l:
        # Nodes are added right to left if layer is odd
        node_at_level = [root.l] + node_at_level if is_odd else node_at_level + [root.l]
        boustrophedon_util(root.l, levels, height)

    # Appends right child if any and recurses that branch
    if root.r:
        # Nodes are added right to left if layer is odd
        node_at_level = [root.r] + node_at_level if is_odd else node_at_level + [root.r]
        boustrophedon_util(root.r, levels, height)

    # Adds current layer's children as value to key = height
    if node_at_level:
        if height not in levels:
            levels[height] = node_at_level
        else:
            # Append in front if the height is odd
            levels[height] = node_at_level + levels[height] if is_odd else levels[height] + node_at_level

    return levels

def boustrophedon(root):
    if not root:
        return None
    levels = {0: [root]}
    levels = boustrophedon_util(root, levels)

    # Sort and flatten each layer's nodes
    res = []
    for i in range(max(levels, key=int) + 1):
        res += levels[i]
    return res


def main():
    rr   = Node(7)
    rl   = Node(6)
    lr   = Node(5)
    ll   = Node(4)
    r    = Node(3, rl, rr)
    l    = Node(2, ll, lr)
    root = Node(1, l, r)

    print(boustrophedon(root))              # Prints [1, 3, 2, 4, 5, 6, 7]

    return

if __name__ == "__main__":
    main()