#!/usr/bin/env python3

"""
18th Feb 2021. #533: Easy

This problem was asked by Facebook.

Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many words as possible that can be formed 
by a sequence of adjacent letters in the grid, using each cell at most once. Given a game board and a dictionary of 
valid words, implement a Boggle solver.

"""

"""
Solution: My solution, which was a variation of this one, but used a stack instead, took more time to complete, so 
this is an alternate solution inspired by the theory at GeeksforGeeks. The solver seems to run much faster in C/C++. 
Another solution involves Trie, but is not much more effective. It can be found here, though:
https://www.geeksforgeeks.org/boggle-set-2-using-trie/

Essentially, we use a depth first search of every possible string that is a valid Boggle formation and compare it to 
the words in the dictionary. A depth first search starts at every node in the Boggle grid, and for each valid neighbor 
(adjacent cell) calls the search function again. If we string along every node value we find on the way, we get a 
Boggle string. Further, we keep track of the cells visited so far in the current traversal so we do not repeat 
neighbors. As every combination given the adjacent constraints is found, the time complexity is O(4 ^ (N ^ 2)).

"""

# Dictionary of valid words
DICT = ["basined",
        "visaed",
        "deaves",
        "deisms",
        "mesian",
        "otherwords"]
N = 3 # max index of the grid
# Grid that shows True if cell has been visited in current potential word
visited = [[False for i in range(N + 1)] for j in range(N + 1)]

# Returns True if word is valid
def is_word(word):
    return word in DICT
  
# Recursively called to append next neighbor to potential word
def find_words_util(boggle, i, j, word=""):
    # Mark current cell as visited, then add value to potential word
    visited[i][j] = True
    word += boggle[i][j]
    
    # This returns valid answers as we find them
    if is_word(word):
        print(word)

    # Find the adjacent positions (x, y) of current cell
    for row in range(max(i - 1, 0), min(i + 1, N) + 1):
        for column in range(max(j - 1, 0), min(j + 1, N) + 1):
            # If neighbor has not been visited, depth first search using this new cell
            if not visited[row][column]:
                find_words_util(boggle, row, column, word)
    # Retrace steps to find alternate paths by removing the last cell added
    word = word[:-1]
    visited[i][j] = False

def find_words(boggle): 
    # Find words starting with every cell in grid
    for i in range(N + 1):
        for j in range(N + 1):
            find_words_util(boggle, i, j)
  
def main():
    boggle = [['s', 'm', 'e', 'p'],
              ['g', 'v', 's', 'x'],
              ['b', 'a', 'i', 'n'],
              ['y', 'd', 'e', 'a']]
  
    find_words(boggle)       # Prints dictionary values

    return

if __name__ == "__main__":
    main()
