#!/usr/bin/env python3

"""
1st Jan 2021. Medium

This problem was asked by Pinterest.

At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). 
To help figure out who this is, you have access to an O(1) method called knows(a, b), 
which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.

"""

"""
Solution: A clever problem because of the limitation on brute force. I felt so smart when it all clicked. 
We have access to n people who could be the celebrity. By splitting them into pairs and testing against the knows method, 
we get enough information to eliminate one of them. Say we try knows(a, b) and it is True. Then a knows b and a cannot be the celebrity.
Alternatively, if it is False, a does not know b and b cannot be the celebrity. 
At the end of the pass, we have a list of length half of n. Continue doing this until only one candidate remains, the elusive celeb.

As this takes n/2 calls to the method in the first pass, and half of the previous number of calls every pass after that, we have a O(n).

"""

def knows(known, a, b):             # Returns True if a knows b
    if b in known[a]:
        return True
    return False

def find_celeb(known):
    queue = list(known.keys())      # Get only the keys (list of n people at party)

    while len(queue) > 1:           
        if knows(known, queue[0], queue[1]):
            queue.pop(0)            # Remove a if a knows b (the celebrity doesn't know anyone at the party)
        else:
            queue.pop(1)            # Remove b if a does not know b (everyone at the party knows the celebrity)

    return queue[0]                 # Return the only remaining candidate in the list

def main():
    known = {                       # Key points to the person, value to who they know at the party
    'a' : {'b', 'c', 'd'},
    'b' : set(),
    'c' : {'b', 'd'},
    'd' : {'b'}
    }

    print("The celebrity is", find_celeb(known))

    return

if __name__ == "__main__":
    main()

