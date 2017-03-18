# 각각의 차이점은?
# list comprehension: s1를 계산하기 위해서는 sum 함수는 next()함수를 list에 대해서 10**6만큼 호출해야 함
# 단점: sum()함수를 호출하기 전에 list 전체가 먼저 만들어져 있어야 함(time and space 낭비)
s1 = sum([n ** 2 for n in range(10 ** 6)])

# s2, s3: generator expression
s2 = sum((n ** 2 for n in range(10 ** 6)))  #note: s2, s3는 같음 s2에서의 ()은 불필요함
s3 = sum(n ** 2 for n in range(10 ** 6))

print(s1 == s2 == s3)
