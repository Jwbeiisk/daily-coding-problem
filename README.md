# daily-coding-problem
Doing a code everyday. Probably.

Solutions to problems at dailycodingproblem.com in the order I receive them. Since the dates aren't enough to find these problems again later, I've linked them all here for a quick word search.

---

## Problems

---

### Jan 2021

#### 1

This problem was asked by **Pinterest** (#486: Medium).

At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.

[Solve It!](jan-2021/Jan1.py)

---

#### 2

This problem was asked by **Yext** (#487: Medium).

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

This problem was asked by **Netflix** (#488: Hard).

Implement a queue using a set of fixed-length arrays.

The queue should support enqueue, dequeue, and get_size operations.

[Solve It!](jan-2021/Jan3.py)

---

#### 4

This problem was asked by **Google** (#489: Easy).

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array \[5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is \[5, 2, 3, 4, 1].

[Solve It!](jan-2021/Jan4.py)

---

#### 5

This problem was asked by **Yelp** (#490: Medium).

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

This problem was asked by **Palantir** (#491: Easy).

Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.

[Solve It!](jan-2021/Jan6.py)

---

#### 7

This problem was asked by **Google** (#492: Medium).

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

[Solve It!](jan-2021/Jan7.py)

---

#### 8

This problem was asked by **Triplebyte** (#493: Medium).

You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.

[Solve It!](jan-2021/Jan8.py)

---

#### 9

This problem was asked by **Facebook** (#494: Medium).

Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

[Solve It!](jan-2021/Jan9.py)

---

#### 10

This problem was asked by **Facebook** (#495: Medium)

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

[Solve It!](jan-2021/Jan10.py)

---

#### 11

This problem was asked by **Pivotal** (#496: Easy).

Write an algorithm that finds the total number of set bits in all integers between 1 and N.

[Solve It!](jan-2021/Jan11.py)

---

#### 12

This problem was asked by **Yahoo** (#497: Medium).

Recall that a full binary tree is one in which each node is either a leaf node, or has two children. 
Given a binary tree, convert it to a full one by removing nodes with only one child.
For example, given the following tree:

                         0
                      /     \
                    1         2
                  /            \
                3                4
                  \            /   \
                    5         6     7
You should convert it to:

                     0
                  /     \
                5         4
                        /   \
                       6     7
               
[Solve It!](jan-2021/Jan12.py)

---

#### 13

This problem was asked by **WhatsApp** (#498: Easy).

Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for the 
entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3).

[Solve It!](jan-2021/Jan13.py)

---

#### 14

Daily Coding Problem skipped an email through some glitch. I've made a **sudoku solver** instead here.

[Solve It!](jan-2021/Jan14.py)

---

#### 15

This problem was asked by **Palantir** (#499: Easy).

A typical American-style crossword puzzle grid is an N x N matrix with black and white squares, which obeys the following rules:

Every white square must be part of an "across" word and a "down" word.
No word can be fewer than three letters long.
Every white square must be reachable from every other white square.
The grid is rotationally symmetric (for example, the colors of the top left and bottom right squares must match).

Write a program to determine whether a given matrix qualifies as a crossword grid.

[Solve It!](jan-2021/Jan15.py)

---

#### 16

This problem was asked by **Google** (#500: Easy).

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

        [[f, f, f, f],
         [t, t, f, t],
         [f, f, f, f],
         [f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

[Solve It!](jan-2021/Jan16.py)


---

#### 17

This problem was asked by **Facebook** (#501: Medium).

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that 
shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.

[Solve It!](jan-2021/Jan17.py)

---

#### 18

This problem was asked by **PayPal** (#502: Easy).

Given a binary tree, determine whether or not it is height-balanced. A height-balanced binary tree can be defined as one in which 
the heights of the two subtrees of any node never differ by more than one.

[Solve It!](jan-2021/Jan18.py)

---

#### 19

This problem was asked by **Google** (#503: Medium).

Given a linked list, sort it in O(n log n) time and constant space. For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.

[Solve It!](jan-2021/Jan19.py)

---

#### 20

This problem was asked by **Twitter** (#504: Easy).

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, 
with the following API:

record(order_id): adds the order_id to the log

get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

[Solve It!](jan-2021/Jan20.py)

---

#### 21

This problem was asked by **Amazon** (#505: Easy).

Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.

[Solve It!](jan-2021/Jan21.py)

---

#### 22

This problem was asked by **Fitbit** (#506: Medium).

Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form. For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.

[Solve It!](jan-2021/Jan22.py)

---

#### 23

This problem was asked by **Uber** (#507: Easy).

On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file. Write a program that reads this file as a stream and returns the top 3 candidates at any given time. If you find a voter voting more than once, report this as fraud.

[Solve It!](jan-2021/Jan23.py)

---

#### 24

This problem was asked by **Dropbox** (#508: Medium).

Create an algorithm to efficiently compute the approximate median of a list of numbers.

More precisely, given an unordered list of N numbers, find an element whose rank is between N / 4 and 3 * N / 4, with a high level of certainty, in less than O(N) time.

[Solve It!](jan-2021/Jan24.py)

---

#### 25

This problem was asked by **Quora** (#509: Medium).

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

[Solve It!](jan-2021/Jan25.py)

---

#### 26

This problem was asked by **Airbnb** (#510: Hard).

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].

[Solve It!](jan-2021/Jan26.py)

---

#### 27

This problem was asked by **Yelp** (#511: Medium).

You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward from that element. Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.

[Solve It!](jan-2021/Jan27.py)

---

#### 28

This problem was asked by **Google** (#512: Medium).

You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true. Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

[Solve It!](jan-2021/Jan28.py)

---

#### 29

This problem was asked by **Lyft** (#513: Medium).

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

[Solve It!](jan-2021/Jan29.py)

---

#### 30

This problem was asked by **Microsoft** (#514: Medium).

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4. Your algorithm should run in O(n) complexity.

[Solve It!](jan-2021/Jan30.py)

---

#### 31

This problem was asked by **LinkedIn** (#515: Medium).

Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.

[Solve It!](jan-2021/Jan31.py)

---
