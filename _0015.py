#!/usr/bin/env python3
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?
def fac(n):
    val = 1
    while n >= 1:
        val *= n
        n -= 1
    return val

def no_combinations(n,k):
    return fac(n) // (fac(k) * fac(n-k))

for size in range(1,21):
    print("no combinations of {size}x{size}: {combos}".format(size=size, combos=max(no_combinations(2*size,i) for i in range(2*size))))
