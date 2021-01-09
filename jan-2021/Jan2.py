#!/usr/bin/env python3

"""
2nd Jan 2021. Medium

This problem was asked by Yext.

Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. 
For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6
Given a binary tree and a particular node, find all cousins of that node.

"""

"""
Solution: Cousins are characterized by two features. 
One, they are at the same level as the particular node. A level/depth is the number of branches from the root to the current node.
Two, they do not share the same parent as the particular node.

"""

class Node:                                     # Basic Node with left and right branch
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Find:
    def __init__(self):
        self.level   = 1
        self.cousins = []
        self.parent  = None

    def _parent(self, root, node):              # Recursively traverses tree to find the parent and level of node
        self.level += 1                         
        if root.left == node:
            self.parent = root
            return True
        elif root.right == node:
            self.parent = root
            return True                         # Checks if current node is the parent of picked node

        if type(root.left) == Node:
            if self._parent(root.left, node):
                return True                     # Checks left branches for parent nodes
        if type(root.right) == Node:
            if self._parent(root.right, node):
                return True                     # Checks right branches for parent nodes

        self.level -= 1
        return

    def _level(self, root, lev):                # Recursively finds all nodes at the same level as lev
        if lev == 1:
            self.cousins.append(root)
        if type(root) == Node:
            self._level(root.left, lev - 1)
            self._level(root.right, lev - 1)

        # List of cousins now show data and nodes with same parent or None are removed
        return [x.data for x in self.cousins if x not in [self.parent.right, self.parent.left, None]]
        

def find_cousin(root, node):
    f = Find()
    f._parent(root, node)                       # Finds nodes parents
    if f.parent == None:
        return "Node not found or is root."

    cousins = f._level(root, f.level)           # Find nodes of same level

    if cousins != []:      
        return cousins
    return "No cousins."                        # Prints "no cousins" if none are found
    

def main():
    root = Node(1)                              # Creating a binary tree
    p1 = Node(2)
    p2 = Node(3)
    c1 = Node(4)
    c2 = Node(5)
    c3 = Node(6)

    root.left = p1
    root.right = p2
    p1.left = c1
    p1.right = c2
    p2.right = c3

    print(find_cousin(root, c1))                # Prints cousins of 4 if any

    return

if __name__ == "__main__":
    main()




