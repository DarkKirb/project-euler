#!/usr/bin/env python3
# cython: language_level=3
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?
from libs import primes


def uniqify(a, b):
    counts = dict()
    for i in a:
        counts[i] = counts.get(i, 0) + 1
    for i in b:
        counts[i] = counts.get(i, 0) + 1
    retlist = []
    for key, value in counts.items():
        retlist.extend((key,) * value)
    return retlist
factors = []
for i in range(2, 21):
    factors = uniqify(factors, primes.factorOutGenerator(i))

final = 1
for i in factors:
    final = final * i
print(final)
