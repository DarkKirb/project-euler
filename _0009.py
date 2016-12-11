#!/usr/bin/env python3
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 5².
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def triple(hi):
    for n in range(hi):
        for m in range(n):
            yield n**2 - m**2, 2*n*m, n**2 + m**2

for a,b,c in triple(10000):
    if a+b+c == 1000:
        print(a,"*",b,"*",c,"=",a*b*c)
        break
