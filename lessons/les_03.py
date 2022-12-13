class Poligon:
    name = 'Poligon'
    all = []

    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0] * no_of_sides
        self.all.append(self)

    def __str__(self):
        return f'{self.__class__.__name__} {self.sides}'

    # def __repr__(self):
    #     return f'{self.__class__.__name__} {self.sides}'


class Triangle(Poligon):
    # all = []
    name = 'Triangle'

    def __init__(self):
        super().__init__(3)
        print(f'Родитель {super().name}')
        # print('Triangle')
        # self.all.append(self)
        # Triangle.all.append(self) # можно и так, но как выше корректней


class Rect(Poligon):
    # all = []
    name = 'Rect'

    def __init__(self):
        super().__init__(4)
        print(f'Родитель {super().name}')
        # print('Rect')
        # self.all.append(self)
        # Rect.all.append(self) # можно и так, но как выше строчкой - корректнее


# p = Poligon(5)
# print(p)
#
# t = Triangle()
# t = Triangle()
# t = Triangle()
# print(t)
# print(len(Triangle.all))
# print(Rect.all)
#
# r = Rect()
# r = Rect()
# print(r)
# print(len(Rect.all))
# print(Triangle.all)
# print(len(Poligon.all))

p = Poligon(5)

t = Triangle()

r = Rect()
