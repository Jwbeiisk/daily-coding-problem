#!/usr/bin/env python3

"""
5th Mar 2021. #548: Easy

This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

"""

"""
Solution: We can convert distances around the clock into degrees by dividing 360 (the total degrees around the whole 
clock) by 12 (the number of 'whole number' milestones around the clock). Converting the times into the clock hand 
positions now gives us the two sides of the angle we need to find. We can do this by multiplying the difference 
between the two values (the closest around the clock - E.g: we always pick an angle less than 180 degrees) by 360 / 12.

"""

def time_angle(t):
    hour, minute = [int(val) for val in t.split(':')]

    invalid_hour = hour > 24 or hour < 0
    invalid_minute = minute > 59 or minute < 0
    invalid_time = hour == 24 and minute != 0

    if True in [invalid_hour, invalid_minute, invalid_time]:
        return None

    angle = 360 / 12
    minute /= 5
    hour %= 12

    diff = abs(hour - minute)
    diff = min(diff, (12 - diff))

    return round(diff * angle)

def main():
    time1 = "04:30"
    time2 = "12:00"

    print(time_angle(time1), "degrees")         # Prints 60 degrees (4 to 6)
    print(time_angle(time2), "degrees")         # Prints 0 degrees (12 to 12)
        
    return

if __name__ == "__main__":
    main()