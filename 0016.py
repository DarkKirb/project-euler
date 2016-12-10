#!/usr/bin/env python3
#2¹⁵ = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2¹⁰⁰⁰?
print(sum((int(i) for i in list(str(2**1000)))))
