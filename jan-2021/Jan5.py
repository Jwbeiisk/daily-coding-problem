#!/usr/bin/env python3

"""
5th Jan 2021. Medium

This problem was asked by Yelp.

The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

The horizontal distance of the root is 0.
The horizontal distance of a left child is hd(parent) - 1.
The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
The bottom view of a tree, then, consists of the lowest node at each horizontal distance. 
If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.

"""

"""
Solution: We can use a dictionary to store the hd and values of nodes that will appear in the bottom view. 
Since the bottom view has multiple right answers (when two nodes are at the same depth and hd), 
we overwrite the hd value as we traverse the tree. To traverse the tree, 
a queue makes sure both the hd and the right and left brnaches of nodes are explored.

"""

class Node:                                             # Basic Node structure with data and right and left branches
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = None

def bottom_view(root):
    tree_dict = dict()                                  # Contains each hd away from root and the most recent node at that distance
    to_explore = [root]                                 # Queue of nodes to be traversed to find bottommost node  
    root.hd = 0

    while (to_explore != []):
        current_node = to_explore.pop(0)                # Current node is the next node if taken depth-wise and left to right 
        tree_dict[current_node.hd] = current_node.data  # Dict stores the hd and currently bottommost node at that hd

        if type(current_node.left) == Node:             # Store the children of current node, its hd relative to current node (+/-1)
            current_node.left.hd = current_node.hd - 1
            to_explore.append(current_node.left)

        if type(current_node.right) == Node:
            current_node.right.hd = current_node.hd + 1
            to_explore.append(current_node.right)

    # Returns node data against sorted hd (leftmost to rightmost)
    return [tree_dict[x] for x in sorted(tree_dict.keys())]

def main():
    root = Node(5)                                      # Basic Binary Tree Construction
    a1 = Node(3)
    a2 = Node(7)
    b1 = Node(1)
    b2 = Node(4)
    b3 = Node(6)
    b4 = Node(9)
    c1 = Node(0)
    c2 = Node(8)

    root.left = a1
    root.right = a2
    a1.left = b1
    a1.right = b2
    a2.left = b3
    a2.right = b4
    b1.left = c1
    b4.left = c2

    print(bottom_view(root))                            # Prints bottom view of tree

    return


if __name__ == "__main__":
    main()