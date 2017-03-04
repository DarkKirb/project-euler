#!/usr/bin/env python3
# Find the sum of all the positive integers which cannot be written as the
# sum of two abundant numbers.
import math
abundant = []


def factor_gen(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            if i == n // i:
                yield i
            else:
                yield i
                yield n // i


def is_abundant(n):
    global abundant
    if n in abundant:
        return True
    abund = sum(factor_gen(n)) > n
    if abund:
        abundant.append(n)
    return abund


def abundant_gen(n):
    for i in abundant:
        if i >= n:
            return
        yield i


def abundant_sum(n):
    if not n % 100:
        print(n)
    """Finds an abundant sum with that sum"""
    for i in abundant_gen(n):
        if n - i in abundant:
            return (i, n - i)
    return None

for i in range(28123):
    is_abundant(i)
print(sum(((x if abundant_sum(x) == None else 0) for x in range(1, 28123))))
