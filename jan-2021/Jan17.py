#!/usr/bin/env python3

"""
17th Jan 2021. Medium

This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that 
shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.

"""

"""
Solution: See also: Fisher-Yates shuffle algorithm. We have a function get_random that returns a random number between 1 and an input 
k. For a given deck of length deck_size, we consider the last element, and get a random index from get_random(deck_size). We swap the 
last element with the random index (which could be the last index itself). Now we exclude the ast index and do the same for 
(deck_size - 1) elements, where get_random has input (deck_size - 1). Continue this till the first element to get a shuffled deck.

"""

import random


def get_random(k):
    return random.randrange(1, k + 1)               # Returns a random integer between 1 and k (inclusive)


def get_swap_card(deck_size):                       # Returns an index between 0 and deck_size - 1
    return get_random(deck_size) - 1, (deck_size - 1)


def swap(deck, a, b):                               # Swaps two cards at indices a and b in deck
    deck[a], deck[b] = deck[b], deck[a] 
    return


def shuffle_deck(deck_size):                        # Creates a deck from 1 to deck_size, returns shuffled deck
    deck = [x for x in range(1, deck_size + 1)]

    while(deck_size):                               # Card to be swapped is considered from the last element to the first
        b, deck_size = get_swap_card(deck_size)     # We only consider possible swaps to elements before the card selected
        swap(deck, deck_size, b)

    return deck


def main():
    deck_size = 52                                  # Number of cards in a deck

    print(shuffle_deck(deck_size))                  # Prints shuffled deck

    return


if __name__ == "__main__":
    main()