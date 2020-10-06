import time
import functools

# Rekurencja

@functools.lru_cache(128)
def fibo_rek(n):
    if n<=1:
        return n
    else:
        return fibo_rek(n-2) + fibo_rek(n-1)

@functools.lru_cache(128)
def fibo_loop(n):
    a, b = 0,1
    for _ in range(n):
        a, b = b, a+b
    return a

print(fibo_rek(10), fibo_loop(10))

ts1 = time.time()
for _ in range(1000):
    fibo_rek(20)
ts2 = time.time()
print(ts2-ts1)

ts1 = time.time()
for _ in range(1000):
    fibo_loop(20)
ts2 = time.time()
print(ts2-ts1)