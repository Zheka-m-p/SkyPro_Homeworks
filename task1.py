import math
from scipy.misc import derivative


class Derivative:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        # считает производную с помощью функции из модуля scipy.misc
        # derivative(функция, точка где считать производную, точность(если я правильно понял) или приращение аргумента)
        # или это уже готовое решение для находждения f'(x)?
        return derivative(self.__func, args[0], dx=1e-5)  #


@Derivative
def sin_(x):
    return math.sin(x)
    # return math.cos(x)

sin_(math.pi / 3)
print(sin_(math.pi / 3))
##0.4999566978958203 такое в примере, у меня чуть ближе к верному значению для косинусa pi/3
