class MyInt:
    def __init__(self, value):
        if type(value) is str and not value.isdigit():
            raise TypeError('В числе не может быть никаких символов кроме цифр!')
        self.__value = value

    def __str__(self):
        """Возвращает на печать в виде строки"""
        return str(self.__value)
        # return f'{self.__value}'

    # блок для сложение, позволяет складывать числа и строки, строчки и числа и много раз в одном присваивании
    def __add__(self, other):
        """Позволяет добавлять число или строку справа(если она идёт вторым в сложении)"""
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__value + other)

    def __radd__(self, other):
        """Позволяет добавлять число или строку слева(если она идёт первым в сложении)"""
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__value + other)

    def __iadd__(self, other):
        """Позвлояет добавлять сложение командой '+=' без перезаписи экземпляра класса """
        # Не нужно для реализации 3 задачи
        if isinstance(other, str):
            other = int(other)
        self.__value = self.__value + other
        return self

    # блок для вычитания, позволяет вычитать числа и строки, строчки и числа и много раз в одном присваивании
    def __sub__(self, other):
        """Позволяет вычитать число из строки справа(если она идёт вторым в вычитании)"""
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__value - other)

    def __rsub__(self, other):
        """Позволяет вычитать строку из числа слева(если она идёт первым в вычитании)"""
        if isinstance(other, str):
            other = int(other)
        return MyInt(other - self.__value)

    def __isub__(self, other):
        """Позвлояет вычитать  командой '-=' без перезаписи экземпляра класса """
        # Не нужно для реализации 3 задачи
        if isinstance(other, str):
            other = int(other)
        self.__value = self.__value - other
        return self

    # блок для умножения, позволяет умножать числа и строки, строчки и числа и много раз в одном присваивании
    def __mul__(self, other):
        """Позволяет умножать число на строку справа(если она идёт вторым в умножении)"""
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__value * other)

    def __rmul__(self, other):
        """Позволяет умножать строку на число слева(если она идёт первым в умножении)"""
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__value * other)

    def __imul__(self, other):
        """Позвлояет умножать командой '*=' без перезаписи экземпляра класса """
        # Не нужно для реализации 3 задачи
        if isinstance(other, str):
            other = int(other)
        self.__value = self.__value * other
        return self

    # блок для деления, позволяет делить числа и строки, строчки и числа и много раз в одном присваивании
    def __truediv__(self, other):
        """Позволяет делить число на строку справа(если она идёт вторым в делении)"""
        if isinstance(other, str):
            other = int(other)
        return MyInt(self.__value / other)

    def __rtruediv__(self, other):
        """Позволяет делить строку на число слева(если она идёт первым в делении)"""
        if isinstance(other, str):
            other = int(other)
        return MyInt(other / self.__value)

    def __itruediv__(self, other):
        """Позвлояет делить  командой '+=' без перезаписи экземпляра класса """
        # Не нужно для реализации 3 задачи
        if isinstance(other, str):
            other = int(other)
        self.__value = self.__value / other
        return self


a = MyInt(5)
print(a) # 5
a = a + '5'
print(a) # 10
a = a - 2 - 3
print(a) # 5
a = a * '5'
print(a) # 25
a = a / 10
print(a) # 2.5
# b = MyInt('dfs11') # ругаца будет) raise TypeError('В числе не может быть никаких символов кроме цифр!')
