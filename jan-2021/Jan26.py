#!/usr/bin/env python3

"""
26th Jan 2021. #510: Hard

This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].

"""

"""
Solution: Although not a trivial solution, this method of creating Tries is overall more scalable, and impressive. 
https://fizzbuzzed.com/top-interview-questions-5/ does a better job of explaining the solution. I had initially worked 
out a simpler solution through brute force, but it would not have been very efficient.

"""

from collections import defaultdict

class Trie:
    def __init__(self):
        self.paths = defaultdict(Trie)
        self.end_index = -1
        self.contains_palindrome = []

    def add_word(self, word, index):
        trie = self
        for i, c in enumerate(reversed(word)):
            if is_palindrome(word[0 : len(word) - i]):
                self.contains_palindrome.append(index)
            trie = trie.paths[c]
        trie.end_index = index

def make_trie(words):
    trie = Trie()
    for i, word in enumerate(words):
        trie.add_word(word, i)
    return trie

def is_palindrome(word):
    return word == word[::-1]

def get_palindrome(trie, word, index):
    output = []
    while word:
        if trie.end_index >= 0:
            if is_palindrome(word):
                output.append(trie.end_index)
        if not word[0] in trie.paths:
            return output
        trie = trie.paths[word[0]]
        word = word[1:]

    if trie.end_index >= 0:
        output.append(trie.end_index)
    output.extend(trie.contains_palindrome)
    return output

def palindrome_pair(words):
    trie = make_trie(words)
    output = []
    for i, word in enumerate(words):
        candidates = get_palindrome(trie, word, i)
        output.extend([[i, c] for c in candidates if i != c])
    return output

def main():
    words = ["code", "edoc", "da", "d"]
    
    print(palindrome_pair(words))           # Returns [[0, 1], [1, 0], [2, 3]]

    return

if __name__ == "__main__":
	main()
