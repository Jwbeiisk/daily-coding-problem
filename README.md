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

### Feb 2021

#### 1

This problem was asked by **Zillow** (#516: Medium).

Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. 

Create an algorithm to find the nth sevenish number.

[Solve It!](feb-2021/Feb1.py)

---

#### 2

This problem was asked by **Google** (#517: Easy).

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

[Solve It!](feb-2021/Feb2.py)

---

#### 3

This problem was asked by **Microsoft** (#518: Easy).

Given an array of numbers and a number k, determine if there are three entries in the array which add up to the specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.

[Solve It!](feb-2021/Feb3.py)

---

#### 4

This problem was asked by **Facebook** (#519: Medium).

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.

[Solve It!](feb-2021/Feb4.py)

---

#### 5

This problem was asked by **LinkedIn** (#520: Hard).

You are given a binary tree in a peculiar string representation. Each node is written in the form (lr), where l corresponds to the left child and r corresponds to the right child.

If either l or r is null, it will be represented as a zero. Otherwise, it will be represented by a new (lr) pair.

Here are a few examples:

        A root node with no children: (00)
        A root node with two children: ((00)(00))
        An unbalanced tree with three consecutive left children: ((((00)0)0)0)

Given this representation, determine the depth of the tree.

[Solve It!](feb-2021/Feb5.py)

---

#### 6

This problem was asked by **PayPal** (#521: Medium).

Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

            t     a     g
             h   s z   a
              i i   i z
               s     g
               
[Solve It!](feb-2021/Feb6.py)

---

#### 7

This problem was asked by **Microsoft** (#522: Medium).

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].

[Solve It!](feb-2021/Feb7.py)

---

#### 8

This problem was asked by **Jane Street** (#523: Easy).

Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

        a + b = M
        a XOR b = N
    
[Solve It!](feb-2021/Feb8.py)

---

#### 9

This problem was asked by **Amazon** (#524: Medium).

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements. Do this in O(N) time.

[Solve It!](feb-2021/Feb9.py)

---

#### 10

This problem was asked by **Amazon** (#525: Easy).

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

        [[1,  2,  3,  4,  5],
         [6,  7,  8,  9,  10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]

You should print out the following:

        1
        2
        3
        4
        5
        10
        15
        20
        19
        18
        17
        16
        11
        6
        7
        8
        9
        14
        13
        12
    
[Solve It!](feb-2021/Feb10.py)

---

#### 11

This problem was asked by **Yahoo** (#526: Easy).

You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string daily and k = 1. The best we can create in this case is ailyd.

[Solve It!](feb-2021/Feb11.py)

---

#### 12

This problem was asked by **Amazon** (#527: Medium).

Huffman coding is a method of encoding characters based on their frequency. Each letter is assigned a variable-length binary string, such as 0101 or 111110, where shorter lengths correspond to more common letters. To accomplish this, a binary tree is built such that the path from the root to any leaf uniquely maps to a character. When traversing the path, descending to a left child corresponds to a 0 in the prefix, while descending right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

            *
          /   \
        *       *
       / \     / \
      *   a   t   *
     /             \
    c               s

With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and use it to determine a mapping between characters and their encoded binary strings.

[Solve It!](feb-2021/Feb12.py)

---

#### 13

This problem was asked by **Microsoft** (#528: Easy).

Write a program to determine how many distinct ways there are to create a max heap from a list of N given integers.

For example, if N = 3, and our integers are [1, 2, 3], there are two ways, shown below.

      3      3
     / \    / \
    1   2  2   1

[Solve It!](feb-2021/Feb13.py)

---

#### 14

This problem was asked by **Google** (#529: Hard).

Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].

[Solve It!](feb-2021/Feb14.py)

---

#### 15

This problem was asked by **Google** (#530: Easy).

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

[Solve It!](feb-2021/Feb15.py)

---

#### 16

This problem was asked **Microsoft** (#531: Easy).

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

[Solve It!](feb-2021/Feb16.py)

---

#### 17

This problem was asked by **Google** (#532: Medium).

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

    (0, 0)
    (1, 2)
    (2, 2)
    (4, 0)

The board would look like this:

    [b 0 0 0 0]
    [0 0 b 0 0]
    [0 0 b 0 0]
    [0 0 0 0 0]
    [b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

[Solve It!](feb-2021/Feb17.py)

---

#### 18

This problem was asked by **Facebook** (#533: Easy).

Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid, using each cell at most once. Given a game board and a dictionary of valid words, implement a Boggle solver.

[Solve It!](feb-2021/Feb18.py)

---

#### 19

This problem was asked by **Amazon** (#534: Easy).

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.

[Solve It!](feb-2021/Feb19.py)

---

#### 20

This problem was asked by **Goldman Sachs** (#535: Medium).

You are given N identical eggs and access to a building with k floors. Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be 5.

[Solve It!](feb-2021/Feb20.py)

---

#### 21

This problem was asked by **Google** (#536: Medium).

Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

        5
       / \
      3   7
     / \   \
    2   4   8

[Solve It!](feb-2021/Feb21.py)

---

#### 22

This problem was asked by **Apple** (#537: Easy).

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

    if n is even, the next number in the sequence is n / 2
    if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?

[Solve It!](feb-2021/Feb22.py)

---

#### 23

This problem was asked by **LinkedIn** (#538: Hard).

Given a set of characters C and an integer k, a De Bruijn sequence is a cyclic sequence in which every possible k-length string of characters in C occurs exactly once.

For example, suppose C = {0, 1} and k = 3. Then our sequence should contain the substrings {'000', '001', '010', '011', '100', '101', '110', '111'}, and one possible solution would be 00010111.

Create an algorithm that finds a De Bruijn sequence.

[Solve It!](feb-2021/Feb23.py)

---

#### 24

This problem was asked by **Pandora** (#539: Easy).

Given an undirected graph, determine if it contains a cycle.

[Solve It!](feb-2021/Feb24.py)

---

#### 25

This problem was asked by **Morgan Stanley** (#540: Easy).

In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

           1
        /     \
      2         3
     / \       / \
    4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].

[Solve It!](feb-2021/Feb25.py)

---

#### 26

This problem was asked by **Amazon** (#541: Easy).

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

[Solve It!](feb-2021/Feb26.py)

---

#### 27

This problem was asked by **Dropbox** (#542: Medium).

Given an undirected graph G, check whether it is bipartite. Recall that a graph is bipartite if its vertices can be divided into two independent sets, U and V, such that no edge connects vertices of the same set.

[Solve It!](feb-2021/Feb27.py)

---

#### 28

This problem was asked by **Google** (#543: Medium).

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

[Solve It!](feb-2021/Feb28.py)

---

### Mar 2021

#### 1

This problem was asked by **Google** (#544: Hard).

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

[Solve It!](mar-2021/Mar1.py)

---

#### 2

This problem was asked by **Twitter** (#545: Hard).

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

[Solve It!](mar-2021/Mar2.py)

---

#### 3

This problem was asked by **Google** (#546: Medium).

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

    There is 1 smaller element to the right of 3
    There is 1 smaller element to the right of 4
    There are 2 smaller elements to the right of 9
    There is 1 smaller element to the right of 6
    There are no smaller elements to the right of 1

[Solve It!](mar-2021/Mar3.py)

---

#### 4

This problem was asked by **Salesforce** (#547: Hard).

Given an array of integers, find the maximum XOR of any two elements.

[Solve It!](mar-2021/Mar4.py)

---

#### 5

This problem was asked by **Microsoft** (#548: Easy).

Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

[Solve It!](mar-2021/Mar5.py)

---
