class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gemail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
# John
# John.Smith@gemail.com
# John Smith

emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email) #note: 다른 값이 나옴
print(emp_1.fullname())
# Jim
# John.Smith@gemail.com
# Jim Smith