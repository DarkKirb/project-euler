#!/usr/bin/env python3
# cython: language_level=3
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
table = []


def collatz(n):
    global table
    x = 0
    while not n == 1:
        if n <= len(table):
            x += table[n - 1]
            break
        x += 1
        if n % 2:
            n = 3 * n + 1
        else:
            n = n // 2
    table.append(x)
    return x
high = 0
for i in range(1, 1000000):
    this = collatz(i)
    high = max(high, this)
    if high == this:
        print("Current highest:", i)
