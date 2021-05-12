#!/usr/bin/env python3

"""
8th Mar 2021. #551: Medium

This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also 
not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.

"""

"""
Solution: Assume two tosses from a biased function that returns 0 with the probability x and 1 with the possibility 
(1-x). The probability of getting a 0 then a 1 is x * (1-x) and the probability of getting a 1 then a 0 is (1-x) * x. 
These two products result in the same answer, i.e: with equal probability. Therefore, if we get this pattern, we can 
return one of the tosses (always return the same one).

If we didn't get a pattern of (0, 1) or (1, 0), we call the same function again.

"""

from random import randint
# A random bias for toss_biased (constant every time this program is run)
RAND_BIAS = randint(0, 1) * 50 + randint(1, 49)

def toss_biased():
    # Returns a biased toss
    return 1 if randint(0, 100) <= RAND_BIAS else 0

def toss_unbiased():
    toss1, toss2 = toss_biased(), toss_biased()
    # Returns True if the tosses are (0, 1) or (1, 0)
    if toss1 ^ toss2:
        return toss1
    # Get new tosses if tosses are (0, 0) or (1, 1)
    return toss_unbiased()

def main():
    print(sum([toss_biased() for _ in range(99999)]) / 99999)       # Returns a random bias (0 to 1)
    print(sum([toss_unbiased() for _ in range(99999)]) / 99999)     # Returns a bias very close to 0.5
        
    return

if __name__ == "__main__":
    main()