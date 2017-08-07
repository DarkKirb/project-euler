#!/usr/bin/env python3
def is_pandigital(a,b,c):
    s=str(a) + str(b) + str(c)
    if "0" in s:
        return False
    for i in range(1,10):
        if s.count(str(i)) != 1:
            return False
    return True

products=[]

for x in range(10,100):
    for y in range(100, 1000):
        s=x*y
        if is_pandigital(x,y,s) and s not in products:
            products.append(s)

for x in range(1, 10):
    for y in range(1000, 10000):
        s=x*y
        if is_pandigital(x,y,s) and s not in products:
            products.append(s)

print(sum(products))
