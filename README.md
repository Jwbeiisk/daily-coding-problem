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

This problem was asked by **Palantir** (Easy).

Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.

[Solve It!](jan-2021/Jan6.py)

---

#### 7

This problem was asked by **Google** (Medium).

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

[Solve It!](jan-2021/Jan7.py)

---

#### 8

This problem was asked by **Triplebyte** (Medium).

You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.

[Solve It!](jan-2021/Jan8.py)

---

#### 9

This problem was asked by **Facebook** (Medium).

Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

[Solve It!](jan-2021/Jan9.py)

---

#### 10

This problem was asked by **Facebook** (Medium)

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

[Solve It!](jan-2021/Jan10.py)

---

#### 11

This problem was asked by **Pivotal** (Easy).

Write an algorithm that finds the total number of set bits in all integers between 1 and N.

[Solve It!](jan-2021/Jan11.py)

---

#### 12

This problem was asked by **Yahoo** (Medium).

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
               
[Solve It!](jan-2021/Jan12.py)

---

#### 13

This problem was asked by **WhatsApp** (Easy).

Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for the 
entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3).

[Solve It!](jan-2021/Jan13.py)

---

#### 14

This problem was asked by **Palantir** (Easy).

A typical American-style crossword puzzle grid is an N x N matrix with black and white squares, which obeys the following rules:

Every white square must be part of an "across" word and a "down" word.
No word can be fewer than three letters long.
Every white square must be reachable from every other white square.
The grid is rotationally symmetric (for example, the colors of the top left and bottom right squares must match).

Write a program to determine whether a given matrix qualifies as a crossword grid.

[Solve It!](jan-2021/Jan14.py)

---

#### 15

This problem was asked by **Google** (Easy).

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
 [t, t, f, t],
 [f, f, f, f],
 [f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

[Solve It!](jan-2021/Jan15.py)

---
