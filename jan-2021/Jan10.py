#!/usr/bin/env python3

"""
10th Jan 2021. Medium

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

"""

"""
Solution: Instead of storing all the elements in memory, we assign probabilities to each index in the stream. 

The probability that one of the elements has the highest random number generated associated with it is 1 / length of the stream, 
which is a uniform probability.

"""

import random

def get_random_element(stream):                         # This logic could also work with just indices, instead of the entire stream
    max_prob = random.random()                          # Random number generated (0.0 - 1.0) for the first element
    rand = stream[0]                                    # Currently selects the first element of stream

    for i in range(1, len(stream) + 1):                 # For every index in stream, generate a random number, prob
        prob = random.random()
        if prob > max_prob:
            rand = stream[i - 1]                        # If this is the highest rolled number, store it as return value
            max_prob = prob

    return rand

def main():
    stream = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    print(get_random_element(stream))

    return

if __name__ == "__main__":
    main()