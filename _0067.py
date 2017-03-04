#!/usr/bin/env python3
# cython: language_level=3
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:
import json
with open("data/triangle.json") as f:
    triangle = json.load(f)
# NOTE: As there are only 16384 routes, it is possible to solve this
# problem by trying every route. However, Problem 67, is the same
# challenge with a triangle containing one-hundred rows; it cannot be
# solved by brute force, and requires a clever method! ;o)


def bruteforce():
    global triangle
    for y in range(98, -1, -1):  # last row is already inited
        for x in range(y + 1):
            triangle[y][x] += max(triangle[y + 1][x], triangle[y + 1][x + 1])

bruteforce()
print(triangle[0][0])
