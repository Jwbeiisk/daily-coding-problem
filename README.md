# daily-coding-problem
Doing a code everyday. Probably.

Solutions to problems at dailycodingproblem.com in the order I receive them. Since the dates aren't enough to find these problems again later, I've linked them all here for a quick word search.

---

## Problems

---

### Jan 2021

#### 1

This problem was asked by **Pinterest***.

At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.

[Solve It!](jan-2021/Jan1.py)

---

#### 2

This problem was asked by **Yext**.

Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6
Given a binary tree and a particular node, find all cousins of that node.

---

#### 3

This problem was asked by **Netflix**.

Implement a queue using a set of fixed-length arrays.

The queue should support enqueue, dequeue, and get_size operations.

---

#### 4

This problem was asked by **Google**.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array \[5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is \[5, 2, 3, 4, 1].

---

#### 5

This problem was asked by **Yelp**.

The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

The horizontal distance of the root is 0.
The horizontal distance of a left child is hd(parent) - 1.
The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
The bottom view of a tree, then, consists of the lowest node at each horizontal distance. If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be \[0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.

---

#### 6

This problem was asked by **Palantir**.

Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.

---

