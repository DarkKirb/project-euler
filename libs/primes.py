import math
primes=[2]

def prime(hi):
    # Not designed to be fast.
    global primes
    for n in primes:
        if n >= hi:
            return
        yield n
    for n in range(primes[-1]+1, hi):
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

def isPrime(n):
    p=0
    for p in prime(n+1):
        pass
    if p == n:
        return True
    return False


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
