import timeit

def fibonacci1(n):
    if n <= 1: return n
    return fibonacci1(n - 1) + fibonacci1(n - 2)

def fibonacci2(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

t1 = timeit.Timer("fibonacci1(10)", "from __main__ import fibonacci1")
t2 = timeit.Timer("fibonacci2(10)", "from __main__ import fibonacci2")

print t1.timeit(1000);
print t2.timeit(1000);