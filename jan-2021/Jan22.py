#!/usr/bin/env python3

"""
22nd Jan 2021. #506: Medium

This problem was asked by Fitbit.

Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form. 
For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.

"""

"""
Solution: Not sure if the linked list input will always be sorted to begin with, which is why I've included a merge sort first. 
Without the sort, it takes O(n) time to go through the list and alternate every two values. For a sorted list, we simply swap 
data from a node and its next node. By leaving the first node untouched, this method works for both odd and even length lists.

"""


class Node:                             # Basic linked list node with data and next, prints data value
    def __init__(self, data):
        self.data = data
        self.next = None
        return

    def __repr__(self):
        return self.data


class LinkedList:                       # Linked list with alternate method, prints entire list
    def __init__(self):
        self.head = None
        return

    def __repr__(self):
        node  = self.head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def alternate(self):
        if self.head.next:              # Make changes only if list longer than one entry, first mergesort
            self.head = a = self.sort(self.head)
            while a.next and a.next.next:
                a.next.data, a.next.next.data = a.next.next.data, a.next.data
                a = a.next.next         # Swap the two nodes after a, change a to point to the last node swapped this way
        return

    # This part is not required if the list is always in order to begin with
    def sort(self, head):               # Merge sort where list is recursively split in two, then merged in order
        if head.next:
            mid = fast = head
            while fast.next and fast.next.next:
                mid  = mid.next
                fast = fast.next.next

            left  = head
            right = mid.next
            mid.next = None

            L = self.sort(left)
            R = self.sort(right)

            new_ptr = new_head = Node(-1)
            new_head.next = new_ptr
            while L and R:
                if L.data < R.data:
                    new_ptr.next = L
                    new_ptr = new_ptr.next
                    L = L.next
                else:
                    new_ptr.next = R
                    new_ptr = new_ptr.next
                    R = R.next

            while L:
                new_ptr.next = L
                new_ptr = new_ptr.next
                L = L.next
            while R:
                new_ptr.next = R
                new_ptr = new_ptr.next
                R = R.next

            return new_head.next
        return head


def main():
    list1 = LinkedList()
    list1.head = n1 = Node(1)
    n1.next    = n2 = Node(2)
    n2.next    = n3 = Node(3)
    n3.next    = n4 = Node(4)
    n4.next         = Node(5)
    print("Input:", list1)              # Prints 1 -> 2 -> 3 -> 4 -> 5

    list1.alternate()
    print("Output:", list1)             # Prints 1 -> 3 -> 2 -> 5 -> 4

    return


if __name__ == "__main__":
    main()
