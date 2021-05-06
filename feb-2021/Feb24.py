#!/usr/bin/env python3

"""
24th Feb 2021. #539: Easy

This problem was asked by Pandora.

Given an undirected graph, determine if it contains a cycle.

"""

"""
Solution: BFS of a grid created from the list of edges gives us an easier way of determining if a graph is cyclic.

"""

class Graph:
    def __init__(self, edges):
        self.nodes = [[] for _ in range(len(edges) + 1)]
 
        for (src, dest) in edges:
            self.nodes[src].append(dest)
            self.nodes[dest].append(src)

def bfs(graph, N):
    visited = [False] * N
    visited[1] = True
    q = []
    q.append((1, -1))

    while q:
        (cell_a, start) = q.pop(0)
 
        for cell_b in graph.nodes[cell_a]:
            if not visited[cell_b]:
                visited[cell_b] = True
                q.append((cell_b, cell_a))
 
            elif cell_b != start:
                return True
    return False
 
 
def main():
    edges = [(0, 1), (1, 2), (2, 3), (0, 2)]

    graph = Graph(edges)
    print(bfs(graph, len(edges) + 1))

if __name__ == "__main__":
    main()