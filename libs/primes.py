import math


def prime(hi):
    # Not designed to be fast.
    primes = [2]
    yield 2
    for n in range(3, hi):
        upper = int(math.sqrt(n))
        out = False
        for d in primes:
            if d > upper:
                break
            if not n % d:
                out = True
        if not out:
            primes.append(n)
            yield n


def factorOutGenerator(n):
    for d in prime(n + 1):
        if n <= 1:
            return
        while n % d == 0:
            yield d
            n //= d


def divisorGenerator(n):
    for d in range(1, n):
        if n % d == 0:
            yield d


def factorOut(n):
    return list(factorOutGenerator(n))
