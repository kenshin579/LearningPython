def adder(*n):
    return sum(n)


s1 = sum(map(lambda n: adder(*n), zip(range(100), range(1, 101))))
print(s1)
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
print(s2)

# test
print(list(zip(range(100), range(1, 101))))
print(list(map(lambda n: adder(*n), zip(range(100), range(1, 101)))))


def fahrenheit(T):
    return ((float(9) / 5) * T + 32)


temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
print(temperatures_in_Fahrenheit)

f1 = map(lambda n: ((float(9) / 5) * n + 32), temperatures)
print(list(f1))
