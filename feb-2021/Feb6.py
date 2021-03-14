#!/usr/bin/env python3

"""
6th Feb 2021. #521: Medium

This problem was asked by PayPal.

Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out 
diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

    t     a     g
     h   s z   a
      i i   i z
       s     g

"""

"""
Solution: We create k number of lines that store the string to be printed out in the final zigzag. We iterate through 
every character in the string, following the path of the zig zag by appending the character to the line we are 
currently at. Every other line has a single space appended to it. We change the slope (whether we are moving up or 
down the zigzag) whenever we reach one of the ends.

Finally, printing out each string in order of their line number gives us the output.

E.g: after the first k iterations, in this example, we would have letters = ['t   ', ' h  ', '  i ', '   s'].

"""

def zigzag(sentence, k):
    row = 0                                         # Which row of the zigzag a character must be appended
    slope = 1                                       # Whether the zigzag is moving up or down
    letters = [''] * k                              # A string corresponding to each line of the final output

    for char in range(len(sentence)):               # Iterate through every letter
        for line in range(k):
            if row == line:                         # Append the next character only to letter[row], else append " "
                letters[line] += sentence[char]
            else:
                letters[line] += " "

        row += slope                                # Change slope to -1 to climb up the zigzag, update row
        if row in [0, k - 1]:
            slope *= -1

    return "\n".join(letters)                       # Return newline separated lines in letters

def main():
    sentence = "thisisazigzag"
    k = 4

    print(zigzag(sentence, k))

    return

if __name__ == "__main__":
    main()