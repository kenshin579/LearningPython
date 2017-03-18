from math import sqrt

# this will generate all possible pairs
mx = 10
legs = [(a, b, sqrt(a ** 2 + b ** 2))
        for a in range(1, mx) for b in range(a, mx)]
# this will filter out all non pythagorean triples
print(legs)
legs = list(
    filter(lambda triple: triple[2].is_integer(), legs))

print(legs)  # prints: [(3, 4, 5.0), (6, 8, 10.0)] # note: int, float 넘거가 섞여있어서 이거를 다음에 제거해보
