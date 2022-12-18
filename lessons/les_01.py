class Animal:
    @staticmethod
    def make_sound():
        raise NotImplementedError('Метод make_sound() должен быть переопределен в дочернем классе')

class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"cat {self.name}, {self.age} years old")

    @staticmethod
    def make_sound():
        print('Meow')

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"dog {self.name}, {self.age} years old")

    @staticmethod
    def make_sound():
        print('Gav')

cat1 = Cat('Kitty', 10)
dog1 = Dog('Sharik', 4)
#
# cat1.cat_info()
# cat1.make_meow()
#
# dog1.dog_info()
# dog1.make_gav()

for animal in (cat1, dog1):
    animal.info()
    animal.make_sound()


