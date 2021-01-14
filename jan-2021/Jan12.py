#!/usr/bin/env python3

"""
12th Jan 2021. Medium

This problem was asked by Yahoo.

Recall that a full binary tree is one in which each node is either a leaf node, or has two children. 
Given a binary tree, convert it to a full one by removing nodes with only one child.

For example, given the following tree:

         0
      /     \
    1         2
  /            \
3                 4
  \             /   \
    5          6     7
You should convert it to:

     0
  /     \
5         4
        /   \
       6     7
"""

"""
Solution: We queue each node as we find it when we traverse levels from root. For each node, we store the parent and 
direction from parent that this node is a branch of (e.g: We store Node(5), Node(0) as parent and 1 (left branch) as 
direction). If we find a node that is not full, we find which branch has a child and make it the child of the selected 
node's parent with the direction of the selected node's branch. This cuts the selected node out of the tree.

"""

class Node:                                              # Basic node class for binary tree
    def __init__(self, data = None):
        self.data = data
        self.l    = None
        self.r    = None


def full_tree(root, parent = None, direction = None):    # Can search below any node, not just root
    queue = [[root, parent, direction]]                  # Store root in queue

    while(queue != []):
        [node, parent, direction] = queue.pop(0)         # Consider a selected node

        if node.r == None and node.l == None:            # If leaf, pass
            continue

        elif node.r != None and node.l != None:          # If full, store children in queue, with parent info
            queue.append([node.l, node, 1])
            queue.append([node.r, node, 0])

        else:                                            # If not full, find single child and connect to parent
            child = node.r if node.r != None else node.l # Store right branch as child if node, else left
            if direction: parent.l = child               # Child is now parent's left branch is direction, else right branch
            else: parent.r = child
            queue.append([child, parent, direction])     # Store child in queue, with new parent info

    return root

def print_tree(root, tab = 0):                           # Prints a primitive tree diagram
    print("    " * max(tab - 1, 0), "...." * min(tab, 1), root.data, sep="")
    if root.l:
        print_tree(root.l, tab + 1)
    if root.r:
        print_tree(root.r, tab + 1)

    return

def main():
    root = Node(0)                                       # Create a basic binary tree
    p1   = Node(1)
    p2   = Node(2)
    q1   = Node(3)
    q2   = Node(4)
    r1   = Node(5)
    r2   = Node(6)
    r3   = Node(7)
    s1   = Node(8)

    root.l = p1
    root.r = p2
    p1.l   = q1
    p2.r   = q2
    q1.r   = r1
    q2.l   = r2
    q2.r   = r3

    print("Input tree:")
    print_tree(root)
    print("Output tree:")
    print_tree(full_tree(root))                          # Call function that converts to full tree

    return

if __name__ == "__main__":
    main()