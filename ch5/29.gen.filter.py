cubes = [x ** 3 for x in range(10)]

# list compression
odd_cubes1 = filter(lambda cube: cube % 2, cubes)
print(type(odd_cubes1))
print(list(odd_cubes1))

# generator expression
odd_cubes2 = (cube for cube in cubes if cube % 2)
print(type(odd_cubes2))
print(list(odd_cubes2))