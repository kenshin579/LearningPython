people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
result = list(zip(people, ages))
print(result)

for person, age in zip(people, ages):
    print(person, age)
