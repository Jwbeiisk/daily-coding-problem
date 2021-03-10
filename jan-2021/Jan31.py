#!/usr/bin/env python3

"""
31st Jan 2021. #515: Medium

This problem was asked by LinkedIn.

Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before 
nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.

"""

"""
Solution: We create two lists to account for the elements lesser than the pivot and the rest of the linked list input. Appending the latter gives us a suitable solution.

"""


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
 

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def append(self, data):
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def print_list(self):
        node = self.head
        while node:
            print node.data,
            print "->",
            node = node.next
        print "Null"


def pivot_list(l, k):
    lesser = LinkedList()
    greater = LinkedList()

    node = l.head
    while node:
        if k > node.data:
            lesser.append(node.data)
        else:
            greater.append(node.data)
        node = node.next
    lesser.tail.next = greater.head
    lesser.print_list()
    return


def main():
    l = LinkedList()
    l.append(5)
    l.append(1)
    l.append(8)
    l.append(0)
    l.append(3)
    l.print_list()              # Returns 5 -> 1 -> 8 -> 0 -> 3

    k = 3

    pivot_list(l, k)            # Returns 1 -> 0 -> 5 -> 8 -> 3

    return

if __name__ == "__main__":
    main()
