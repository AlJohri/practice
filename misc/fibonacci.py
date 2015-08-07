import timeit

from functools import lru_cache

def fibonacci1(n):
    if n <= 1: return n
    return fibonacci1(n - 1) + fibonacci1(n - 2)

@lru_cache(maxsize=None)
def fibonacci2(n):
    if n <= 1: return n
    return fibonacci2(n-1) + fibonacci2(n-2)

def fibonacci3(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

t1 = timeit.Timer("fibonacci1(10)", "from __main__ import fibonacci1")
t2 = timeit.Timer("fibonacci2(10)", "from __main__ import fibonacci2")
t3 = timeit.Timer("fibonacci3(10)", "from __main__ import fibonacci3")

print(t1.timeit(1000))
print(t2.timeit(1000))
print(t3.timeit(1000))

print(fibonacci2.cache_info())