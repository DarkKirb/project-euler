#!/usr/bin/env python3
# cython: language_level=3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
from libs import primes
print(list(primes.factorOutGenerator(600851475143))[-1])
