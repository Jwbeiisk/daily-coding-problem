#!/usr/bin/env python3

"""
20th Jan 2021. Easy

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, 
with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.

"""

"""
Solution: We use a class that holds a list of logs, and does not grow longer than the length N. The reversed index gives us the last 
ith log.

"""

class Log:
    def __init__(self, N):
        self.length = N
        self.ids = []
        return

    def record(self, order_id):
        if len(self.ids) == self.length:        # Pops first id if length exceeds N
            self.ids.pop(0)
        self.ids.append(order_id)
        return

    def get_last(self, i = 1):
        if i > self.length:                     # i must be less than N
            return None

        return self.ids[self.length - i]        # Returns last ith element

def main():
    l = Log(3)
    l.record(1111)
    l.record(2222)
    l.record(3333)
    l.record(4444)                              # Pops 1111
    print(l.get_last(1))                        # Returns 4444
    print(l.get_last(4))                        # Returns None (i > N)
    print(l.get_last(3))                        # Returns 2222

    return

if __name__ == "__main__":
    main()