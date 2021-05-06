#!/usr/bin/env python3

"""
27th Feb 2021. #542: Medium

This problem was asked by Dropbox.

Given an undirected graph G, check whether it is bipartite. Recall that a graph is bipartite if its vertices can be 
divided into two independent sets, U and V, such that no edge connects vertices of the same set.

"""

"""
Solution: A list of edges tell us the connecting vertices of the graph. We can expand this into a 2D array, where each 
element in the array contains an array of all the vertices the vertex of the same index connects to. 

E.g: if the edges contain pairs (1, 0), (0, 3), (5, 0), then the first element of the graph array would be [1, 3, 5] 
as 0 connects to all these vertices.

Now to check if the graph is bipartite, we have two sets, a and b and start putting vertices in a (E.g: 0) and the 
vertices connecting to it (E.g: 1, 3, 5) in b. This is done unless the vertex already belongs to a set. 

Finally, we iterate through set b to find any nodes connecting to each other (we do not have to check group a as the 
graph shows undirected connections; if the graph is bipartite it would always cause a contradiction in group b first).

"""


# Contains a list of all connecting vertices for each vertex
class Graph:
    def __init__(self, edges):
        self.nodes = [[] for _ in range(len(edges))]

        for (src, dest) in edges:
            self.nodes[src].append(dest)
            self.nodes[dest].append(src)


# Returns True if bipartite
def is_bipartite(graph):
    grp_a = set()
    grp_b = set()

    # Iterate through every vertex
    for i in range(len(graph.nodes)):
        # If the node is already assigned to group b, skip vertex
        if i in grp_b:
            continue
        # Else add to group a and all connecting vertices to group b
        grp_a |= set([i])
        if graph.nodes[i]:
            for dest in graph.nodes[i]:
                grp_b |= set([dest])

    # Check if no edges connect vertices of group b (both source and dest in group b)
    for i in grp_b:
        if graph.nodes[i]:
            for dest in graph.nodes[i]:
                if dest in grp_b:
                    return False
    return True


def main():
    non_bipartite_edges = [(0, 1), (1, 2), (2, 3), (0, 2)]
    bipartite_edges = [(1, 5), (2, 5), (3, 6), (4, 2), (5, 1), (5, 2), (6, 2)]

    non_bipartite_graph = Graph(non_bipartite_edges)
    bipartite_graph = Graph(bipartite_edges)

    print(is_bipartite(non_bipartite_graph))            # Prints False
    print(is_bipartite(bipartite_graph))                # Prints True
    
    return


if __name__ == "__main__":
    main()