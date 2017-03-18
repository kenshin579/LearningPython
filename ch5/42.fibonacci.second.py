def fibonacci(N):
    """Return all fibonacci numbers up to N. """
    yield 0 #note: 결과 0을 반환함
    if N == 0:
        return #note: 0이면 StopIteration이 발생함 -> Stop됨
    a = 0
    b = 1
    while b <= N:
        yield b #note: loop을 돌면서 b의 값을 반환함
        a, b = b, a + b

print(list(fibonacci(0)))  # [0]
print(list(fibonacci(1)))  # [0, 1, 1]
print(list(fibonacci(50)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
