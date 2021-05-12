#!/usr/bin/env python3

"""
7th Mar 2021. #550: Hard

This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a 
possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any 
currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.

"""

"""
Solution: Solution from https://github.com/deboracornetta/algorithms/blob/master/src/currency_arbitrage.py

Jane Street Puzzles are hard, and this one involves some math. For simplicity's sake, we return true if the end result 
anywhere is larger than 1, meaning we start out with A = 1.

We first get every permutation for each row in the 2D array. Then we try to carry out the most profitable transaction 
using the order from the permutation. This makes sure we cover all possibilities to potentially make a profit.

"""

from itertools import permutations

def all_permutations(rates):
    for length in range(2, len(rates) + 1):
        for sequence in permutations(range(len(rates)), length):
            yield sequence

def execute(sequence, rates):
    amount = 1
    current_symbol = sequence[0]
    sequence = *sequence[1:], sequence[0]

    for next_symbol in sequence:
        rate = rates[current_symbol][next_symbol]
        amount *= rate
        current_symbol = next_symbol

    return amount

def is_stonks(rates):
    for sequence in all_permutations(rates):
        if 1 < execute(sequence, rates):
            return True
    return False

def main():
    rates1 = [
        [1,    2,     3],
        [0.5,  1,     4],
        [0.5,  0.25,  1]
    ]

    rates2 = [
        [1,  0,  0],
        [0,  1,  0],
        [0,  0,  1]
    ]

    print(is_stonks(rates1))            # Prints True
    print(is_stonks(rates2))            # Prints False
        
    return

if __name__ == "__main__":
    main()