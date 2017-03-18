A = 100

# note: list, dict, set comprehesions, generator expression에서 A의 global값은 변경되지 않음
ex1 = [A for A in range(5)]
print(A)  # prints: 100

ex2 = list(A for A in range(5))
print(A)  # prints: 100

ex3 = dict((A, 2 * A) for A in range(5))
print(A)  # prints: 100

ex4 = set(A for A in range(5))
print(A)  # prints: 100

s = 0
for A in range(5): # note: for에서는 변경이 됨
    s += A
print(A)  # prints: 4
