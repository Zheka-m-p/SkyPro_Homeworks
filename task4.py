class MyInt:
    def __init__(self, value):
        if type(value) is str and not value.isdigit():
            raise TypeError('В числе не может быть никаких символов кроме цифр!')
        self.__value = int(value)

    def __str__(self):
        """Возвращает на печать в виде строки"""
        return str(self.__value)

    @classmethod
    def __check_data(cls, other):
        if not isinstance(other, (int, str, MyInt)):
            raise TypeError('Должен быть тип str, int или класс MyInt')
        return int(other) if isinstance(other, (int, str)) else other.__value

    def __eq__(self, other):
        oth = self.__check_data(other)
        return self.__value == oth

    def __ne__(self, other):
        oth = self.__check_data(other)
        return self.__value != oth

    def __lt__(self, other):
        oth = self.__check_data(other)
        return self.__value < oth

    def __le__(self, other):
        oth = self.__check_data(other)
        return self.__value <= oth

    def __gt__(self, other):
        oth = self.__check_data(other)
        return self.__value > oth

    def __ge__(self, other):
        oth = self.__check_data(other)
        return self.__value >= oth


a = MyInt('6')
b = MyInt(4)
print(a == b)  # False
print(a != b)  # True
print(a >= b)  # True
print(a < b)  # False
print('Далее проверка не с классом MyInt')
print(a == '5')  # False
print(a != 5)  # True
print(a < '3')  # False
print(a <= 6)  # True
print(a >= 5)  # True
print(a > '7')  # False

c = MyInt('fdaf')  # TypeError: В числе не может быть никаких символов кроме цифр!
