# class User: #  слотс - это взаиомдействие с атрибутами из экземпляров класса
# А если мы пропишем проперти(гетер и сетер) то мы можем работать с атрибутами КЛАССА. поэтому так можно
# и нет никаких противоречий
#     __slots__ = ('name', 'surname', '__fio')
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.__fio = name + ' ' + surname
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, value):
#         self.__fio = value
#
# x = User('Ivan', 'Ivanov')
# x.name
# x.fio = 'Elena Ivanov'
# x.fio
class User:
    __slots__ = ('name', 'surname') #, '__fio')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        # self.__fio = name + ' ' + surname

class User2(User):
    __slots__ = ('age',)

u = User2('Ivan', 'Ivanov')
u.name
u.surname
# u.middle_name = 'Ivanovich' # можно создать, если не прописать __slots__ = ()  в дочернем классе
u.name = 'da'
# u.__dict__ #нет дикта уже, если прописали слотс в дочернем классе
u.age = 24 # будет работать. если записать 'age'  в кортеж slots
