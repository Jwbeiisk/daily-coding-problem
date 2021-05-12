#!/usr/bin/env python3

"""
11th Mar 2021. #554: Easy

This problem was asked by Palantir.

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 
    4 / 13 
can be represented as 
    1 / 4 + 1 / 18 + 1 / 468

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.

"""

"""
Solution: We get each of these fractions by getting the inverse of the current fraction rounded to the next (higher) 
integer value which is then taken an inverse of again. This new part of the Egyptian fraction is subtracted from the 
current fraction and the process is repeated until the last fraction has 1 as its numerator.

E.g: 4/13 would get its first fraction by first finding 13/4 (3.25) rounded to the next digit (4) and taken as an 
inverse (1/4). This is subtracted from 4/13 (3/52) and the process is done again for this new fraction.

"""

from fractions import Fraction

def egyptian_frac(frac):
    if frac.numerator == 1:
        return [frac]

    e_frac = Fraction(1, int((frac.denominator/frac.numerator) + 1))

    return [e_frac] + egyptian_frac(frac - e_frac)

def main():
    frac = Fraction(4, 13)

    print(egyptian_frac(frac))              # Prints [Fraction(1, 4), Fraction(1, 18), Fraction(1, 468)]
        
    return

if __name__ == "__main__":
    main()