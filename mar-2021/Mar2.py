#!/usr/bin/env python3

"""
2nd Mar 2021. #545: Hard

This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in 
the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as 
the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

"""

"""
Solution: THe example input tree looks like this:

    a
  /   \
 b     c
  \    /
   d  e
       \
        f

Since we have the ability to get a node's parents, we make a list of all the parents of one of the nodes and compare 
it to the parents of the other.

"""


# Binary Tree node with a pointer to its parent
class Node:
    def __init__(self, data, l=None, r=None, p=None):
        self.data = data
        self.l = l
        self.r = r
        self.p = p
        return

    def __str__(self):
        return self.data


# Returns the lowest common ancestor
def lca(v, w):
    parents = []
    # Get all parents of v
    while v:
        parents.append(v)
        v = v.p
    # Compare each parent of w with parents (of v)
    while w:
        if w in parents:
            # This is the lca
            return w
        w = w.p
    # If no lca found
    return None


def main():
    a = Node("a")
    b = Node("b", p=a)
    c = Node("c", p=a)
    d = Node("d", p=b)
    e = Node("e", p=c)
    f = Node("f", p=e)

    a.l = b
    a.r = c
    b.r = d
    c.l = e
    e.r = f

    print(lca(d, f))            # Prints a

    return


if __name__ == "__main__":
    main()