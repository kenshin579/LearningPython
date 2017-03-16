people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
result = list(zip(people, ages, nationalities))

print(result)

for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)
