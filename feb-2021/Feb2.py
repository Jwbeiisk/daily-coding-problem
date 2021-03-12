#!/usr/bin/env python3

"""
2nd Feb 2021. #517: Easy

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

"""

"""
Solution: The trivial solution here (which I had initially implemented) stored all the values of one list in a 
dictionary and compared each node in the second list until a match was found. While this still runs in O(M + N) time, 
it requires variable space as the length of the lists are not definite.

Now, consider how a list with an intersection must be of the same length and point to the same values after the 
intersection has taken place. Thus, we may use the difference in length to discard the nodes in the longer list until 
they are both equal. The rest of the lists may be traversed in parallel to find the first matching node.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def print_list(self):
        node = self.head
        while node:
            print(node.data, " -> ", end="")
            node = node.next
        print("Null")


def intersecting_node(A, B):
    length_A = length_B = 0

    node = A.head                           # Find length of list A
    while node:
        length_A += 1
        node = node.next

    node = B.head                           # Find length of list B
    while node:
        length_B += 1
        node = node.next

    node_A = A.head
    node_B = B.head
    if length_A > length_B:                 # If A is longer than B, the first (len(A) - len(B)) nodes may be discarded
        for i in range(length_A - length_B):
            node_A = node_A.next

    else:                                   # If B is longer than A, the first (len(B) - len(A)) nodes may be discarded
        for i in range(length_B - length_A):
            node_B = node_B.next

    while node_A != node_B:                 # The rest of the list may be traversed in parallel to find the common node
        node_A = node_A.next
        node_B = node_B.next

    return node_A, node_A.data


def main():
    A = LinkedList()
    B = LinkedList()

    A1 = Node(3)
    A2 = Node(7)
    A3 = Node(8)
    A4 = Node(10)
    B1 = Node(99)
    B2 = Node(1)

    A.append(A1)
    A.append(A2)
    A.append(A3)
    A.append(A4)

    B.append(B1)
    B.append(B2)
    B.append(A3)
    B.append(A4)

    A.print_list()                          # 3  -> 7  -> 8  -> 10
    B.print_list()                          # 99  -> 1  -> 8  -> 10

    print(intersecting_node(A, B))          # Prints the node holding 8, A3 (and the value for readability)
    return


if __name__ == "__main__":
    main()