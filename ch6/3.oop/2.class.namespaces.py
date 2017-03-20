class Person():
    species = 'Human' # note: class attributes

print(Person.species)  # Human
Person.alive = True  # Added dynamically!
print(Person.alive)  # True

man = Person()
print(man.species)  # Human (inherited)
print(man.alive)  # True (inherited)

Person.alive = False
print(man.alive)  # False (inherited)

# note: instance attrbutes
man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)  # Darth Vader

print(Person.name)
# This doesn't work. We try to access an instance attribute
# from a class. Doing the opposite works, but this will give
# the following error:
# AttributeError: type object 'Person' has no attribute 'name'
