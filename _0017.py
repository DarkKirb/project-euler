#!/usr/bin/env python3
# cython: language_level=3
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
def writeOut(n):
    singles=["one","two","three","four","five","six","seven","eight","nine"]
    teens=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if n < 10: #single digits
        return singles[n-1]
    if n > 10 and n < 20: #teens
        return teens[n-11]
    if n < 100 and not n % 10:
        return tens[(n//10)-1]
    if n == 100:
        return "onehundred"
    if n == 1000:
        return "onethousand"
    if n > 100:
        first=singles[(n//100)-1]
        second = "hundred"
        third = ""
        if n % 100:
            third = "and"+writeOut(n%100)
        return first+second+third
    return tens[(n//10)-1] + singles[(n%10)-1]

print(sum((len(writeOut(i)) for i in range(1,1001))))
