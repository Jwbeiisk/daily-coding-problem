#!/usr/bin/env python3

"""
12th Feb 2021. #527: Medium

This problem was asked by Amazon.

Huffman coding is a method of encoding characters based on their frequency. Each letter is assigned a variable-length 
binary string, such as 0101 or 111110, where shorter lengths correspond to more common letters. To accomplish this, a 
binary tree is built such that the path from the root to any leaf uniquely maps to a character. When traversing the 
path, descending to a left child corresponds to a 0 in the prefix, while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

            *
          /   \
        *       *
       / \     / \
      *   a   t   *
     /             \
    c               s

With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and use it to determine a mapping between 
characters and their encoded binary strings.

"""

"""
Solution: https://en.wikipedia.org/wiki/Huffman_coding#Basic_technique

"""


# Tree Node
class Node:
    def __init__(self, data, freq, l_child=0, r_child=0):
        self.data = data
        self.freq = freq
        self.huffman_encoding = ''
        self.l_child, self.r_child = l_child, r_child

    def __str__(self):
        return self.data + ' -> ' + self.huffman_encoding


def huffman_tree(char_frequencies):
    nodes = []
    # Build tree from frequencies
    for (data, freq) in char_frequencies.items():
        nodes.append(Node(data, freq))

    # Create an encoding for each node
    while len(nodes) > 1:
        # Sort frequencies to get the least occurring first
        nodes = sorted(nodes, key=lambda x: x.freq)
        l_child = nodes[0]
        r_child = nodes[1]

        # We create a pair of children for the last branch (least frequent nodes)
        l_child.huffman_encoding = 0
        r_child.huffman_encoding = 1

        # This is connected to a new parent whose frequency is the sum of child nodes
        parent = Node(l_child.data + r_child.data, l_child.freq + r_child.freq, l_child, r_child)
        # Remove child nodes from nodes left to be encoded
        nodes.pop(0)
        nodes.pop(0)
        # Add parent as it requires an encoding as well
        nodes.append(parent)
    # Return root
    return nodes[0]

# Recursively gets encoding by adding 0 or 1 based on left or right child
def traverse_tree(node, parent_encoding='', node_encoding='-'):
    # Add parent encoding before own value
    node.huffman_encoding = parent_encoding + node_encoding
    if node.l_child:
        # Add 0 and recurse along left branch if left child exists
        traverse_tree(node.l_child, node.huffman_encoding, '0')
    if node.r_child:
        # Add 1 and recurse along right branch if right child exists
        traverse_tree(node.r_child, node.huffman_encoding, '1')
    # If leaf, node is a character and the encoding may be printed
    if not node.l_child and not node.r_child:
        print(node)



def main():
    char_frequencies = {
        'a': 9,
        'b': 2,
        'c': 3,
        'd': 1,
        'e': 15,
        'f': 7
    }

    root = huffman_tree(char_frequencies)               # Creates tree with most frequent values higher
    traverse_tree(root)                                 # Returns encoding of all characters (E.g: b here is 11011)

    return

if __name__ == "__main__":
    main()