#!/usr/bin/env python3
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
palimdromes=[]
for i in range(100,1000):
    for j in range(i, 1000):
        string=repr(i*j)
        if string[:3] == string[6:2:-1]:
            palimdromes.append(i*j)

print(max(palimdromes))
