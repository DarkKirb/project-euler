#!/usr/bin/env python3
fd=[1,1,2,6,24,120,720,5040,40320,362880]

def factorial_digits(x):
    s = 0
    for d in str(x):
        s += fd[int(d)]

    return s
x=0
for i in range(10,2540160):
    if i == factorial_digits(i):
        x+=i
        print(i)

print(x)
