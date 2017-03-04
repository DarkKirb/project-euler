#!/usr/bin/env python3
# Find the product of the coefficients, a and b, for the quadratic
# expression that produces the maximum number of primes for consecutive
# values of n, starting with n=0

from libs import primes


def intgen():
    x = 0
    while True:
        yield x
        x += 1


def check_quadratic(a, b):
    prims = 0
    for i in intgen():
        if primes.isPrime(i**2 + a * i + b):
            prims += 1
        else:
            return prims

maxi = [0, 0, 0]
for a in range(-1000, 1000):
    for b in range(-1001, 1001):
        prims = check_quadratic(a, b)
        if prims > maxi[2]:
            maxi = [a, b, prims]
            print(maxi)

print(maxi, maxi[0] * maxi[1])
