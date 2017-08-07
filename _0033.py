#!/usr/bin/env python3
from fractions import gcd
nominator=1
denominator=1

def remove_first(s, h):
    i = s.index(h)
    return s[0] if i else s[1]

for d in range(10,100):
    if not (d % 10):
        continue
    for n in range(10,d):
        ds = str(d)
        ns = str(n)
        try:
            if ns[0] in ds:
                f1 = n/d
                f2 = int(ns[1]) / int(remove_first(ds, ns[0]))
                if f1 == f2:
                    print(n,d,f1)
                    nominator *= n
                    denominator *= d
        except:
            pass
        try:
            if ns[1] in ds:
                f1 = n/d
                f2 = int(ns[0]) / int(remove_first(ds, ns[1]))
                if f1 == f2:
                    print(n,d,f1)
                    nominator *= n
                    denominator *= d
        except:
            pass
print(nominator, denominator)
print(denominator//gcd(nominator,denominator))
