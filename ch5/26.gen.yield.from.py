def print_squares(start, end):
    yield from (n ** 2 for n in range(start, end)) #todo: 이건 잘 이해가 안됨

for n in print_squares(2, 5):
    print(n)
