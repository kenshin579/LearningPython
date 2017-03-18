from math import sqrt

mx = 10
legs = [(a, b, sqrt(a ** 2 + b ** 2))
        for a in range(1, mx) for b in range(a, mx)]
legs = filter(lambda triple: triple[2].is_integer(), legs)

# todo: 여기서 print하면 아래 legs는 empty가 된다. 왜?
# print(list(legs)) # prints: [(3, 4, 5.0), (6, 8, 10.0)] #

# this will make the third number in the tuples integer
legs = list(
    map(lambda triple: triple[:2] + (int(triple[2]),), legs))

print(legs)  # prints: [(3, 4, 5), (6, 8, 10)]

# test
a = [0, 1, 2, 3, 4, 5]
b = [(3, 4, 5), (6, 8, 10)]
print(a[1:3])
print(a[:3])
print(a[:2])
print(a[:1])
