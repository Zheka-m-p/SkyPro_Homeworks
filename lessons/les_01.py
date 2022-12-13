class Poligon:
    def __init__(self, sides):
        self.sides = sides

    def displey_sides(self):
        print(self.__class__.__name__)
        for i in range(len(self.sides)):
            print(f'Сторона {i + 1} - {self.sides[i]}')

        # self.displey_area()  # чисто для учебных целей, будет работать ,если вызывать из дочерних классов метод
        # displey_sides то автоматически вызовется и displey_area

# class Triangle:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def displey_sides(self):
#         for i in range(len(self.sides)):
#             print(f'Сторона {i + 1} - {self.sides[i]}')
#
#     def displey_area(self):
#         a, b, c = self.sides
#         p = (a + b + c) / 2
#         print(f'Площадь треугольника: {(p * (p - a) * (p - b) * (p - c)) ** 0.5}')
#
# class Rect:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def displey_sides(self):
#         for i in range(len(self.sides)):
#             print(f'Сторона {i + 1} - {self.sides[i]}')
#
#     def displey_area(self):
#         a, b, *anything = self.sides
#         print(f'Площадь прямоугольника: {a * b}')
class Triangle(Poligon):
    def displey_area(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        print(f'Площадь треугольника: {(p * (p - a) * (p - b) * (p - c)) ** 0.5}')

class Rect(Poligon):
    def displey_area(self):
        a, b, *anything = self.sides
        print(f'Площадь прямоугольника: {a * b}')

p = Poligon([3, 5, 7, 9, 3, 5, 6])
p.displey_sides()

t = Triangle([3, 4, 5])
t.displey_sides()
t.displey_area()

r = Rect([4, 5, 4, 5])
r.displey_sides()
r.displey_area()