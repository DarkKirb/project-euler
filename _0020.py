#!/usr/bin/env python3
# cython: language_level=3
#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!
def fac(x):
    r=1
    while x>1:
        r*=x
        x-=1
    return r
print(sum((int(i) for i in str(fac(100)))))
