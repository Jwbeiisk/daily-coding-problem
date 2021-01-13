# daily-coding-problem
Doing a code everyday. Probably.

Solutions to problems at dailycodingproblem.com in the order I receive them. Since the dates aren't enough to find these problems again later, I've linked them all here for a quick word search.

---

## Problems

---

### Jan 2021

#### 1

This problem was asked by **Pinterest** (Medium).

At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.

[Solve It!](jan-2021/Jan1.py)

---

#### 2

This problem was asked by **Yext** (Medium).

Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. For example, in the following diagram 4 and 6 are cousins.

        1
       / \
      2   3
     / \   \
    4   5   6
Given a binary tree and a particular node, find all cousins of that node.

[Solve It!](jan-2021/Jan2.py)

---

#### 3

This problem was asked by **Netflix** (Hard).

Implement a queue using a set of fixed-length arrays.

The queue should support enqueue, dequeue, and get_size operations.

[Solve It!](jan-2021/Jan3.py)

---

#### 4

This problem was asked by **Google** (Easy).

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array \[5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is \[5, 2, 3, 4, 1].

[Solve It!](jan-2021/Jan4.py)

---

#### 5

This problem was asked by **Yelp** (Medium).

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

[Solve It!](jan-2021/Jan5.py)

---

#### 6

This problem was asked by **Palantir**.

Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.

[Solve It!](jan-2021/Jan6.py)

---

#### 7

This problem was asked by **Google**.

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

[Solve It!](jan-2021/Jan7.py)

---

#### 8

This problem was asked by **Triplebyte**.

You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.

[Solve It!](jan-2021/Jan8.py)

---

#### 9

This problem was asked by **Facebook**.

Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

[Solve It!](jan-2021/Jan9.py)

---

#### 10

This problem was asked by **Facebook**.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

[Solve It!](jan-2021/Jan10.py)
