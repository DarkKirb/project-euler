#!/usr/bin/env python3
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?


def fib():
    yield 0
    a = 0
    b = 1
    while True:
        yield b
        b, a = b + a, b

for i, j in enumerate(fib()):
    if j >= 10**999:
        print(i)
        break
