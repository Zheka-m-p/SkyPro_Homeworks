# class User:
#     pass
#
# User.name = 'Bob'
#
# x = User()
# x.name = 'Tim'
class User:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.fi = 1 # так тоже будет ругаца

x = User('Bob', 40)

User.__dict__

x.__dict__

x.weight = 80

del x.name

x.name

x.name = 'Tim'