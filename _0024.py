#!/usr/bin/env python3
# What is the millionth lexicographic permutation of the digits 0, 1, 2,
# 3, 4, 5, 6, 7, 8 and 9?
import itertools
for i, j in enumerate(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])):
    if i == 999999:
        print(j)
        break
