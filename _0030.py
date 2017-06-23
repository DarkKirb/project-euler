#!/usr/bin/env python3
def viable(x):
    return sum(int(c)**5 for c in str(x)) == x

print(sum((x if viable(x) else 0) for x in range(2,194980)))
