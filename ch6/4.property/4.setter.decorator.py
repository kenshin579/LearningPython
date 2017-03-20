class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.email) #note: email은 실제 함수인데 data attribute처럼 접근가능함
print(emp_1.fullname)
# John
# John.Smith@email.com
# John Smith

emp_1.fullname = 'Frank Oh' #note: setter에 의해서 data attribute처럼 세팅함
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# Jim
# John.Smith@gemail.com
# Jim Smith