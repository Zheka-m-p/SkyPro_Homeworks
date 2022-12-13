class Employee:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f'Сотрудник {self.__name}'


class Developer(Employee):
    def __init__(self, name, lang):
        super().__init__(name)
        self.__lang = lang

    def __str__(self):
        return f'{super().__str__()} пишет на {self.__lang}'
        # return f'{self.__name()} пишет на {self.__lang}' # так не будет доступно


e = Employee('Jon')
print(e.__dict__)
print(e)

d = Developer('Ivan', 'Python')
print(d.__dict__)
print(d)
print()
