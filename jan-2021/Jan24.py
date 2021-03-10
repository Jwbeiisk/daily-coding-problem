#!/usr/bin/env python3

"""
24th Jan 2021. #508: Medium

This problem was asked by Dropbox.

Create an algorithm to efficiently compute the approximate median of a list of numbers.

More precisely, given an unordered list of N numbers, find an element whose rank is between N / 4 and 3 * N / 4, with a high level of certainty, in less than O(N) time.

"""

"""
Solution: We use a method called quicksort, where we repeatedly divide a list into segments greater than, less than 
and equal to a randomly selected pivot. Based on how many elements are in these segments, we can narrow down where our 
median would be and recursively do this over only that segment. This way, we can reiterate over only half (on average) 
of the list every time giving us O(n) time [n + 1/2n + 1/4n + ... = 2n = O(n)].

"""

def quickselect(list1, median_index = 0):
    # Rank of median is half the list index length
    if median_index == 0:
        median_index = len(list1) // 2

    # Returns after recursion
    if len(list1) == 1:
        return list1[0]

    # Random element
    pivot = list1[median_index]

    # Sections of values lesser than, greater than and equal to pivot
    lesser_than_pivot = [x for x in list1 if x < pivot]
    greater_than_pivot = [x for x in list1 if x > pivot]
    pivots = [x for x in list1 if x == pivot]

    # If median rank is lesser than the elements in lesser_than_pivot, recurse only on that section
    if median_index < len(lesser_than_pivot):
        return quickselect(lesser_than_pivot, median_index)
    # If median rank is greater than lesser_than_pivot but lesser than pivots, the median is the pivot
    elif median_index < (len(lesser_than_pivot) + len(pivots)):
        return pivot
    # Else, we search for the median in only the greater_than_pivot section, with the rank of the median recalculated
    else:
        return quickselect(greater_than_pivot, median_index - (len(lesser_than_pivot) + len(pivots)))

def main():
    list1 = [3, 4, 6, 2, 9, 12, 1]  # n = 7, median rank is 4
    list2 = [3, 4, 6, 2, 9, 12]     # n = 6, median rank is 4

    print(quickselect(list1))       # Median is 4
    print(quickselect(list2))       # Median is 6

    return

if __name__ == "__main__":
	main()
