#!/usr/bin/env python3
# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.


def fractionCycle(b):
    remainder = 1 % b
    remainders = [remainder]
    while remainder:
        remainder = (10 * remainder) % b
        if remainder in remainders:
            return len(remainders)
        remainders.append(remainder)
    return 0
maxi = [0, 0]
for i in range(1, 1000):
    if not i % 100:
        print(i)
    f = fractionCycle(i)
    if maxi[1] < f:
        maxi = [i, f]

print(maxi)
