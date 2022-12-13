class Poligon:
    pass


class Triangle(Poligon):
    pass

print(issubclass(Triangle, Poligon))  # True т.е. Triangle дочерний класс от Poligon
print(issubclass(Poligon, Triangle))  # False т.к. порядок важен, Triangle наследутется от Poligon
print(issubclass(Poligon, (Triangle, object)) ) # True, можно несколько параметров куда входит передавать
print(issubclass(int, object))  #True
print(issubclass(bool, int))  #True
p = Poligon()
t = Triangle()
print(isinstance(p, Triangle)) # False
print(isinstance(p, (Triangle, Poligon))) # True, т.к. проверят на вхождение в один из классов и его наследников
print(isinstance(t, Triangle)) # True т.к. экземпляр этого класса
print(isinstance(t, Poligon)) # True т.к. экземпляр дочернего(подкласса, класса Poligon)


class Item:

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



