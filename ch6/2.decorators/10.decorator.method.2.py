def p_decorate(func):
    def func_wrapper(*args, **kwargs): #note: arg, keyword arg를 받을 수 있음
        return "<p>{0}</p>".format(func(*args, **kwargs))

    return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family

my_person = Person()

print(my_person.get_fullname())
