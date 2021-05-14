#!/usr/bin/env python3

"""
16th Mar 2021. #559: Medium

This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

"""

"""
Solution: https://leetcode.com/problems/merge-k-sorted-lists/discuss/844684/Python-solution
A more efficient solution.

"""

import heapq


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def merge_k_lists(lists):
    h = []
    counter = 0

    for ls in lists:
        if not ls:
            continue

        heapq.heappush(h, (ls.data, counter, ls))
        counter += 1

    head = None

    while h:
        _, _, current = heapq.heappop(h)
        head = head or current

        if current.next:
            heapq.heappush(h, (current.next.data, counter, current.next))
            counter += 1

        if h:
            current.next = h[0][2]

    return head


def main():
    e4 = Node(11)
    d4 = Node(9, e4)
    c4 = Node(6, d4)
    b4 = Node(2, c4)
    a4 = Node(0, b4)                            # List 4: [0, 2, 6, 9, 11]

    b3 = Node(8)
    a3 = Node(4, b3)                            # List 3: [4, 8]

    c2 = Node(12)
    b2 = Node(5, c2)
    a2 = Node(3, b2)                            # List 2: [3, 5, 12]

    d1 = Node(13)
    c1 = Node(10, d1)
    b1 = Node(7, c1)
    a1 = Node(1, b1)                            # List 1: [1, 7, 10, 13]

    node = merge_k_lists([a1, a2, a3, a4])      # Result list is ordered from 0 to 13

    while node:
        print(node.data, ' ', end=' ')
        node = node.next
        
    return


if __name__ == "__main__":
    main()