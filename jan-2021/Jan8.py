#!/usr/bin/env python3

"""
8th Jan 2021. Medium

This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1. 
Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], 
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.

"""

"""
Solution: random.random() generates a random number between 0 and 1. 

This means there is a 0.1 possibility that a number between 0.0 and 0.1 is generated by the function. Therefore, by splitting the 
numbers in the range 0.0 to 1.0 into buckets that correspond to each magnitude in the probabilitis list, the probability that the number 
generated is in one of the buckets is proportional to that probability (e.g: the probabilities [0.1, 0.5, 0.2, 0.2] can be split into 
buckets of [0.0-0.1, 0.1-0.6, 0.6-0.8, 0.8-1.0], which is done by adding the previous probabilities). Now we find out which bucket the 
randomly generated number lies in and return the corresponding value from the numbers list.

"""

import random                                           # random.random() generates a random number between 0.0 and 1.0

def get_number(numbers, probabilities):
    cur_prob = 0
    if sum(probabilities) != 1:
        return "Probabilities do not sum up to 1."      # To make sure the probabilities list is exhaustive
    rand = random.random()
    for i in range(len(numbers)):
        cur_prob += probabilities[i]                    # The current bucket for the probabilities is the sum of all previous values
        
        #print(cur_prob, rand)                          # This verifies the program working as intended
        if cur_prob <= rand:
            continue

        return numbers[i]

def main():
    numbers = [1, 2, 3, 4]
    probabilities = [0.1, 0.5, 0.2, 0.2]

    print(get_number(numbers, probabilities))

    return

if __name__ == "__main__":
    main()