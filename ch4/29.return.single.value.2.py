from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, range(1, n + 1), 1)

def sum(a, b):
    return a + b

print(mul(3, 2))
print(reduce(sum, [2, 3, 1, 2]))
f5 = factorial(5)  # f5 = 120
print(f5)
print([factorial(k) for k in range(10)])
