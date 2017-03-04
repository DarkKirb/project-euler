#!/usr/bin/env python3
# cython: language_level=3
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
from libs import primes
numbers = dict()
amicable = []


def checkForAmicable(n):
    global numbers, amicable
    if n in numbers:
        return  # Number was already checked
    divsum = sum(primes.divisorGenerator(n))
    numbers[n] = divsum
    if n == divsum:
        return  # not amicable
    if divsum in numbers:
        return  # Not amicable
    divsum2 = sum(primes.divisorGenerator(divsum))
    numbers[divsum] = divsum2
    if n == divsum2:  # Found amicable
        amicable.append(n)
        amicable.append(divsum)
        print("Found", n, "and", divsum)

for n in range(2, 10000):
    if not n % 100:
        pass
    checkForAmicable(n)

print(sum(amicable))
