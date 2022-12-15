class Item:
    def __init__(self, name, price, quantity=0):
        
        self.__check(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __check(self, name, price, quantity):
        if not isinstance(name, str):
            raise TypeError('Название товара должно быть строкой.')
        if not isinstance(price, (float, int)):
            raise TypeError('Цена товара должна быть числом.')
        if not isinstance(quantity, int):
            raise TypeError('Количество товара должно быть целым числом.')

    def __str__(self):
         return f'{type(self).__name__}({self.name}, {self.price}, {self.quantity})'

class Phone(Item):
    def __init__(self, name, price, quantity=0, broken_phones=0):
        self.broken_phones = broken_phones
        super().__init__(name, price, quantity)
             

phone2 = Phone("iPhone 10", 500, 5, 1)
print(phone2)  # Такой вывод, тк. метод стр не переопредел9ли
