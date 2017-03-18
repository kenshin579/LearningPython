s = 0
for A in range(5): # note: 따로 A의 변수를 정의할 필요가 없음
    s += A
print(A)  # prints: 4
print(globals())

# test
print(type(range(1,3)))