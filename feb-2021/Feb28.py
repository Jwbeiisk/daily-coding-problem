#!/usr/bin/env python3

"""
28th Feb 2021. #543: Medium

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller 
than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

"""

"""
Solution: We have two pointers traversing the linked list. The faster one is k nodes ahead of the other one, so that 
when it reaches the end of the list, the slow pointer contains the node we want. We do this by first traversing k 
nodes with the fast pointer, then the rest of the list at the same rate for both pointers. This takes a single pass as 
both pointers are moved together.

"""


# Linked list node
class Node:
    def __init__(self, data, n=None):
        self.data = data
        self.next = n
        return

    def __str__(self):
        return str(self.data)


# List that can remove a node at any position in list
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        return

    # Returns list data as string
    def __str__(self):
        node = self.head
        l = ""
        while node:
            l += str(node) + " -> "
            node = node.next
        l += "END"
        return l

    # The next pointer of previous node points to the next node, deleting the current node
    def remove(self, del_node):
        node = prev = self.head

        while node:
            if node == del_node:
                prev.next = node.next
                return
            prev = node
            node = node.next

    def find_kth_last(self, k):
        fast = slow = self.head

        # Fast pointer after loop points to kth node in list
        while fast and k:
            fast = fast.next
            k -= 1

        # Both pointers travel at same rate till fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Slow pointer holds node to be deleted
        self.remove(slow)
        return self


def main():
    f = Node(6)
    e = Node(5, f)
    d = Node(4, e)
    c = Node(3, d)
    b = Node(2, c)
    a = Node(1, b)

    l = LinkedList(a)                           # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    k = 2

    print(l)
    print(l.find_kth_last(k))                   # Removes 5 (2nd last node)
    
    return


if __name__ == "__main__":
    main()