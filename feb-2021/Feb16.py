#!/usr/bin/env python3

"""
16th Feb 2021. #531: Easy

This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

"""

"""
Solution: Not completely clear on the wording of this problem. Perhaps an implementation of read7 is expected, which 
would determine if it would be able to resume reading from the last index in a while loop. 

Either way, to read n characters, we let the read7 function iterate the smallest number of times to have a total of 
characters greater than n (i.e: 3 times for 21 characters if n is 20). 

Now there are three cases: the file has less than or equal to n characters, or the file has more than n characters. If 
the file has less than n characters, or n characters or n is divisible by 7, the string at the end of the while loop 
must contain at most n characters. This can be returned as is. Else, we calculate the n modulo 7 (6 if n is 20). 7 
minus this number (1 if n is 20) gives us the number of characters to be removed from the end of the read string.

"""

readN(n):
    s = ""
    while n != 0:
        s += read7("file/path")
        n -=7
    if len(s) <= n:
        return s
    return s[:- (7 - (n % 7))]
