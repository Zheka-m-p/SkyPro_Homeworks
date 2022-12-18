# class Base1:
#     pass
#
# class Base2:
#     pass
#
# class MultiDerived(Base1, Base2):
#     pass
#
# for item in MultiDerived.mro():
#     print(item)
print('Почему именно такой обход ниже?')
# <class '__main__.M'>
# <class '__main__.B'>
# <class '__main__.A'>
# <class '__main__.X'>
# <class '__main__.Y'>
# <class '__main__.Z'>
# <class 'object'>
# class X:
#     pass
#
# class Y:
#     pass
#
# class Z:
#     pass
#
# class A(X, Y):
#     pass
#
# class B(Y, Z):
#     pass
#
# class M(B, A, Z):
#     pass
#
# for item in M.mro():
#     print(item)

class Car:
    def __init__(self, model, color):
        super().__init__()
        self.__model = model
        self.__color = color

class MixLog:
    ID = 0

    def __init__(self):
        print('__init__ MixLog')
        MixLog.ID += 1
        self.id = MixLog.ID

    def print_log(self):
        print(f"{self.id}  из {MixLog.ID} электрокар")


class Ev(Car, MixLog):
    pass

ev1 = Ev('Tesla', 'red')
ev2 = Ev('Tesla', 'blue')
ev3 = Ev('Tesla', 'green')
print(Ev.__mro__)
ev2.print_log()