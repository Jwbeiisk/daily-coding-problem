#!/usr/bin/env python3

"""
7th Jan 2021. Medium

This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, 
write a function to determine whether each vertex in the graph can be colored 
such that no two adjacent vertices share the same color using at most k colors.

"""

"""
Solution: I had to google the meanings of a lot of these words (asking Google the answers to their own questions). 
It's fairly straighforward once the meanings are understood, however I spoiled it for myself by looking at a very elegant solution 
to this. I can't unsee it and it's very efficient as far as I can see. 
Maybe I'll revisit this problem to solve it on my own sometime later.

An adjacency matrix is a 2D array that stores the connection of two vertices in a graph. An undirected graph is symmetric.

For e.g:

  b
 / \
a   d
 \ /
  c

would be translated into an adjacency matrix as:

    a | b | c | d
a | 0 | 1 | 1 | 0
b | 1 | 0 | 0 | 1
c | 1 | 0 | 0 | 1
d | 0 | 1 | 1 | 0

Clearly if we do find a solution where each vertex can be colored so that any adjacent one is not the same color, 
using at most k colors, any k greater than the number of vertices is automatically possible (each vertex is a different color).

Otherwise, we try applying a color to a vertex and check whether it conflicts with any other color. If a valid color exists, we go 
to the next vertex, and try every color (less than k) with this check again. If we have enough colors for each vertex, return True.

The program work recursively, and runs in O(k^N) time (k (max) times for every vertex) and O(k) space (I don't usually mention this 
for programs, but I found it on https://www.dailycodingproblem.com/blog/graph-coloring/ and might include it in future problems).

In this example, the program would assign a color 0 for vertex a (no conflicts), color 0 again for vertex b (conflicts with a), color 
1 for vertex b (no conflict), color 0 again for vertex c (conflicts with a), color 1 for vertex c (no conflict), 
and color 0 for vertex d (no conflict). Since colors now has 4 elements [0, 1, 1, 0] and there are only 2 colors used (0 and 1), 
it returns True.

"""

def colorable(graph, colors):
    last_vertex, last_color = len(colors) - 1, colors[-1]

    # finds the last vertex's adjacent vertices, i < last_vertex as it's symmetric (undirected)
    neighbor_colors = [i for i, adjacent in enumerate(graph[last_vertex]) if adjacent and i < last_vertex]

    for neighbor in neighbor_colors:
        if colors[neighbor] == last_color:                  # Looks for conflicts with any color already assigned
            return False

    return True

def color(graph, k, colors = []):
    if len(colors) == len(graph) or k >= len(graph):        # Every vertex has a color already assigned/trivial solution exists
        return True

    for i in range(k):                                      # Try every possible color
        colors.append(i)                                    # Apply color to new vertex
        if colorable(graph, colors):                        # Checks if this vertex color has no conflicts
            if color(graph, k, colors):                     # Recursively colors all other vertices using this configuration
                return True
        colors.pop()                                        # Conflict exists, so remove color from new vertex

    return False                                            # Exhausted k colors, no solution exists

def main():

    graph = [[0, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [0, 1, 1, 0]]

    k = 3

    print(color(graph, k))

    return

if __name__ == "__main__":
    main()