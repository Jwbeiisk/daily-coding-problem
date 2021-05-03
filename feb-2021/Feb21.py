#!/usr/bin/env python3

"""
21th Feb 2021. #536: Medium

This problem was asked by Google.

Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

        5
       / \
      3   7
     / \   \
    2   4   8

"""

"""
Solution: We iterate the list in reverse, as we can construct the tree from top to bottom this way. We compare the 
last element to a recursively passed value of a greater or lesser limit and the parent. If the child is on the right 
branch, it would lie between the parent (lesser limit) and the greater limit. If the child is on the left branch, it 
would lie between the lesser limit and the parent (greater limit). We continue this until every element has been 
connected into the tree. Once the Node is created, the last element can be popped to allow easier recursion.

"""


# Basic BST Node
class Node:
    def __init__(self, data, l_child=None, r_child=None):
        self.data = data
        self.l = l_child
        self.r = r_child

        return


# Prints tree inorder
def print_tree(head):
    if (head == None) :
        return

    print_tree(head.l) 
    print(head.data, end = " ") 
    print_tree(head.r) 

    return


# Recursive function to split tree into lesser and greater branches
def construct_tree_util(seq, lesser=-999999, greater=999999):
    # If all values are iterated over
    if seq == []:
        return None

    # If the last value in the postorder lies in the range for this branch
    if seq[-1] > lesser and seq[-1] < greater:
        # Remove last value and make it a Node
        data = seq.pop()
        root = Node(data)

        # If there are more values in postorder
        if seq != []:
            # If the last value is greater than current value, it is a right child
            root.r = construct_tree_util(seq, data, greater)
            # If the last value is lesser than the current value, it is a left child
            root.l = construct_tree_util(seq, lesser, data)

        # Return current Node if any
        return root
    return None


def construct_tree(seq):
    # Returns root of created tree
    return construct_tree_util(seq)


def main():
    # Postorder
    seq = [2, 4, 3, 8, 7, 5]

    print_tree(construct_tree(seq))         # Prints inorder view of created tree: 2 3 4 5 7 8

    return


if __name__ == "__main__":
    main()