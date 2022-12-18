import timeit
from functools import partial


class Person:
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email


class PersonTest:
    __slots__ = ('name', 'address', 'email')

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

def get_set_delete(person):
    person.name = person.name[::-1] # Имя наоборот
    person.address = ' '.join(person.address.split()[1:]) # убираем индекс из адреса
    del person.email
    person.email = 'Мой адрес - не дом и не улица, мой адрес - Советский Союз'


def main():
    person = Person("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    person_test = PersonTest("Ivan", "123567 Pushkinskaya ul.", "ivan@mail.ru")
    old = min(timeit.repeat(partial(get_set_delete, person), number=1000000))
    new = min(timeit.repeat(partial(get_set_delete, person_test), number=1000000))
    print(f"Текущая реализация: {old}")
    print(f"Тестовая реализация: {new}")
    print(f"Улучшение производительности: {(old - new) / old:.2%}")


if __name__ == "__main__":
    main()

# примерно такая работа должна быть. каждый раз проценты +- скачут
# Текущая реализация: 0.42923599999999995
# Тестовая реализация: 0.35793039999999987
# Улучшение производительности: 16.61%