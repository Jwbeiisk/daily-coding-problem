#!/usr/bin/env python3

"""
15th Mar 2021. #558: Medium

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.

"""

"""
Solution: We sample random points that would appear in the first quadrant of the coordinate axes. The points lie 
between 0 and 1 and may lie inside a circle of radius 1 with its origin at (0, 0) if it satisfies the condition x^2 + 
y^2 <= 1^2 (or r^2). If we have sampled enough of the quarter of the circle uniformly, the ratio of points inside the 
circle and total samples is pi/4. We multiply this by 4 to get an approximate pi.

https://en.wikipedia.org/wiki/Monte_Carlo_method

"""

from random import random, seed

SAMPLES = 999

def monte_carlo_pi():
    prev = 0
    pi = 3
    total_valid_points = 0
    total_points = 0

    # The approximation of pi stays the same for over a couple estimations
    while abs(prev - pi) > 1e-6:
        # Get SAMPLES number of random points with x, y in range(0, 1)
        for _ in range(SAMPLES):
            # Check if random point lies inside a circle of radius 1 with its centre at origin
            if random() ** 2 + random() ** 2 <= 1:
                total_valid_points += 1
            total_points += 1

        prev = pi
        # New estimation is 4 * (pi/4)
        pi = float(4 * total_valid_points) / float(total_points)

    # Return result to 3 decimal places
    return '{0:.3f}'.format(pi)


def main():

    print(monte_carlo_pi())         # Prints 3.142
        
    return

if __name__ == "__main__":
    main()