#!/usr/bin/env python3
# cython: language_level=3
from libs import primes
import math
i = 2
x = 1


def divisors(n):
    no = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if not n % i:
            no += 2
    return no
while True:
    x += i
    if not i % 10000:
        print(i)
    if divisors(x) >= 500:
        print(x)
        break
    i += 1
