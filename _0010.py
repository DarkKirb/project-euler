#!/usr/bin/env python3
# cython: language_level=3
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from libs import primes
print(sum(primes.prime(2000000)))
