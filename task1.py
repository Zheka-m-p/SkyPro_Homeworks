import datetime


class Task:
    def __init__(self, content):
        self.__content = content
        self.__data = datetime.datetime.now()
        # self.__data = self.__date('%Y-%m-%d') # подправить вывод даты

    def __repr__(self):
        return f'{self.__content} (создано {self.__data})'

    def __eq__(self, other):
        if not isinstance(other, Task):
            raise NotImplemented
        return self.__content == other.__content

    def __hash__(self):
        return hash(self.__content)

Task('Сделать домашку')

todo_list = set()

todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Выпить кофе'))
todo_list.add(Task('Выйти на пробежку'))
todo_list.add(Task('Сделать домашку'))

for item in todo_list:
    print(item)