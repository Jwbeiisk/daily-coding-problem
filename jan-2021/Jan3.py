#!/usr/bin/env python3

"""
3rd Jan 2021. Hard

This problem was asked by Netflix.

Implement a queue using a set of fixed-length arrays.

The queue should support enqueue, dequeue, and get_size operations.

"""

"""
Solution: Not completely sure what a set of fixed-length arrays would be, but here's the best I could do. 
A classic queue implementation, with some way of keeping the length of the queue fixed. I even made some small implementation of
a pop method, Python makes things a little too easy.

Queues have a First In First Out order. Enqueue adds data at the last used index in the queue. Dequeue removes from the first index, 
and there is probably an even more old school way of doing it (without remove). Memory management would be key here. Get_size returns
the number of filled indices in the queue.

"""

class Queue:
    def __init__(self, length):                     # Make a queue of a given length, first and last indices both point to 0
        self.q = [None] * length
        self.length = length
        self.last_index = 0
        self.first_index = 0
        return

    def enqueue(self, value):                       # Checks if Queue is full, adds value after the last filled index which increments
        if self.last_index < self.length:
            self.q[self.last_index] = value 
            self.last_index += 1
        else:
            print("Queue full.")
        return

    def dequeue(self):                              # Pops the first value and adjusts the index counters and length accordingly
        self.q.append(None)
        tmp = self.q[self.first_index]
        self.q.remove(self.q[self.first_index])
        if self.last_index != 0:                    # Reduces length of the filled queue if possible, else we have an empty queue
            self.last_index -= 1
        else:
            print("Queue empty.")
            return
        return tmp

    def get_size(self):
        return self.last_index - self.first_index   # Queue length is the number of filled indices (difference between counters)

def main():
    q1 = Queue(5)                                   # Queue for 5 values, add 1, 2, 3 in order and pop 1. Final queue is of size 2.
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    print("Popped", q1.dequeue())                     
    print("Queue size", q1.get_size())

    return

if __name__ == "__main__":
    main()