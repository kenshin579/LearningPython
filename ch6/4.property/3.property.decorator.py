class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.email) #note: email은 실제 함수인데 data attribute처럼 접근가능함
print(emp_1.fullname())
# John
# John.Smith@email.com
# John Smith

emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
# Jim
# John.Smith@gemail.com
# Jim Smith