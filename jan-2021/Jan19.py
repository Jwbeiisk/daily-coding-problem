#!/usr/bin/env python3

"""
19th Jan 2021. Medium

This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.

"""

"""
Solution: MergeSort.

"""


class Node:                                         # Basic linked list node with data and next, prints data
    def __init__(self, data):
        self.data = data
        self.next = None
        return

    def __repr__(self):
        return self.data


class LinkedList:                                   # Linked list with a head that prints the whole list using '->'
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

    def sort(self, head):                           # This function needs to input a head because of the way it calls itself
        if head.next:                               # Only if the list contains at least two nodes will a sort be required

            mid = fast = head                       # Find the middle of the list using a fast and slow pointer
            while fast.next and fast.next.next:     # fast points to the last node, mid to the node exactly between fast and head
                mid = mid.next
                fast = fast.next.next

            left = head                             # split the list into two lists down the middle, left and right
            right = mid.next
            mid.next = None

            L = self.sort(left)                     # Sort each half recursively
            R = self.sort(right)

            new_ptr = new_head = Node(-1)           # For the new, sorted list create a head and pointer
            new_head.next = new_ptr

            while L and R:                          # Compare each half's respective element in each list, appending the lower data
                if L.data < R.data:
                    new_ptr.next = L
                    L = L.next
                else:
                    new_ptr.next = R
                    R = R.next
                new_ptr = new_ptr.next

            while L:                                # For the left over elements in either list
                new_ptr.next = L
                new_ptr = new_ptr.next
                L = L.next
            while R:
                new_ptr.next = R
                new_ptr = new_ptr.next
                R = R.next

            return new_head.next                    # Return the now fully sorted list's head
        return head                                 # Return head if list is empty or has one node


def main():
    linked_list = LinkedList()
    n1 = linked_list.head = Node(4)
    n1.next = n2 = Node(1)
    n2.next = n3 = Node(-3)
    n3.next = n4 = Node(99)
    print("Input:", linked_list)                    # Prints 4 -> 1 -> -3 -> 99

    linked_list.head = linked_list.sort(linked_list.head)
    print("Output:", linked_list)                   # -3 -> 1 -> 4 -> 99

    return


if __name__ == "__main__":
    main()