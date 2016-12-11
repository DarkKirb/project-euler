#!/usr/bin/env python3
# cython: language_level=3
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
palindromes=[]
for i in range(100,1000):
    for j in range(i, 1000):
        string=str(i*j)
        if string[:3] == string[6:2:-1]:
            palindromes.append(i*j)

print(max(palindromes))
