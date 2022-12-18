class Employee:
    __slots__ = ('first', 'last')

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}.@gmail.com"

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, value):
        self.first, self.last = value.split()

    @fullname.deleter
    def fullname(self):
        print('__del__', 'Уже работает не рекурсивно, молодец)')
        self.first, self.last = None, None



emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# John
# John.Smith@email.com
# John Smith

emp_1.fullname = "Corey Schafer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# Corey
# Corey.Schafer@email.com
# Corey Schafer

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# None
# None.None@email.com
# None None
