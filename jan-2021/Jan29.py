#!/usr/bin/env python3

"""
29th Jan 2021. #513: Medium

This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

"""

"""
Solution: We start adding every element after a chosen element in the list until that sum equals or exceeds K. If this result is not K, we move on to the next element. This has a time complexity of O(N^2).

"""

def sum_to_k(list1, K):
    for i in range(len(list1)):
        possible_sum = list1[i]

        for j in range(i + 1, len(list1)):
            if possible_sum >= K: break
            possible_sum += list1[j]

        if possible_sum == K:
            return list1[i:j]
    return None

def main():
    list1 = [1, 2, 3, 4, 5]
    K = 9

    print(sum_to_k(list1, K))       # Returns [2, 3, 4]

    return

if __name__ == "__main__":
    main()
