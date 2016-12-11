#!/usr/bin/env python3
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def multiples(hi, divisors):
    for i in range(hi):
        for d in divisors:
            if not i % d:
                yield i
                break

print(sum(multiples(1000, [3,5])))
