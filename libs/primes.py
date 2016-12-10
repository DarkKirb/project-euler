def primes(n):
    p = [True] * n
    for i in range(2, n):
        if not p[i]: continue
        for j in range(i+i, n, i):
            p[j] = False
        yield i

def factors(n):
    for d in primes(n//2 + 1):
        if n == 1:
            return
        while n % d == 0:
            yield d
            n //= d
    yield n
            
def factorOut(n):
    return list(factors(n))
