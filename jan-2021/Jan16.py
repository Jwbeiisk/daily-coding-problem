#!/usr/bin/env python3

"""
16th Jan 2021. Easy

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end 
coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. 
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
 [t, t, f, t],
 [f, f, f, f],
 [f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

"""

"""
Solution: Simple BFS, where each tile traversed holds its number of steps from the start. Every tile is evaluated, however, 
which makes this a rather trivial solution. Of course, there is a whole host of algorithms to solve this, each more 
efficient than the previous one.

A BFS stores every neighboring tile in a queue for a selected tile, and numbers it as one step further from the previous 
tile. This means that every option that is an equal number of steps away from the start is calculated before moving on. 
This makes it breadth first. As no tile previously traversed is counted again, we do not account for backtracking. 

A check is made for if the tile reached is the end, and is stored as a possible path. Finally, the smallest value here is 
selected.

"""

def get_tile(matrix, index):                            # Returns the value of matrix element at index tuple
    return matrix[index[0]][index[1]]


def get_neighbor(matrix, tile, offset):                 # Returns the index tuple of a tile + offset (if it exists)
    x_min = tile[1] + offset[1] >= 0
    x_max = tile[1] + offset[1] < len(matrix)
    y_min = tile[0] + offset[0] >= 0
    y_max = tile[0] + offset[0] < len(matrix)

    if x_min and x_max and y_min and y_max:             # Check for matrix edges (since no wrap around)
        return (tile[0] + offset[0], tile[1] + offset[1])
    return None


def find_path_length(matrix, start, end):               
    if get_tile(matrix, start) or get_tile(matrix, end):
        return None                                     # Returns if start or end is a wall

    queue = [start]                                     # Tiles to be evaluated
    possible_paths = []                                 # Paths to the end with number of steps (in case multiple exist)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]     # Potential neighbor tiles
    matrix[start[0]][start[1]] = steps = 1              # Mark the first tile with number of steps (1)

    while(queue != []):                                 # Until every reachable tile is traversed
        cur_tile = queue.pop(0)                         # Remove the first tile in the queue
        if cur_tile == end:                             # This is now a possible path
            possible_paths.append(get_tile(matrix, cur_tile))

        for i in range(4):                              # For each neighbor direction (up, down, left, right)
            neighbor = get_neighbor(matrix, cur_tile, directions[i])
            if neighbor != None:                        # If neighbor does exist
                if not get_tile(matrix, neighbor):      # If neighbor is not a wall
                    matrix[neighbor[0]][neighbor[1]] = get_tile(matrix, cur_tile) + 1
                    queue.append(neighbor)              # Mark neighbor with steps from start, and append to queue

    if possible_paths != []:
        return min(possible_paths) - 1                  # Smallest path length of all possible path lengths
    return None                                         # No path found


def main():
    f      = False
    t      = True
    matrix = [[f, f, f, f],                             # This example should return 7
              [t, t, f, t],
              [f, f, f, f],
              [f, f, f, f]]
    start  = (3, 0)
    end    = (0, 0)

    print("Min steps:", find_path_length(matrix, start, end))

    return


if __name__ == "__main__":
    main()
