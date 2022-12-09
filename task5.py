import datetime


class Task:
    def __init__(self, content):
        self.__content = content
        self.__data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return f'{self.__content} (создано {self.__data})'

    def __eq__(self, other):
        if not isinstance(other, Task):
            raise NotImplemented
        return self.__content == other.__content

    def __hash__(self):
        return hash(self.__content)

    def __bool__(self):
        # print('bool за работой!')
        return bool(self.__content)


class TodoList:
    def __init__(self):
        self.tasks = []


    def __setitem__(self, key, value):
        self.tasks.append(None)
        self.tasks[key] = value

    # def __getitem__(self, item):
    #     return self.tasks[item]

    def __delitem__(self, key):
        del self.tasks[key]

    def __repr__(self):
        return str(self.tasks)

    def __next__(self):  # для моей реализации пришлось ещё __len__ определять
        if self.value >= len(self.tasks) - 1:
            raise StopIteration('А всё. Элементы кончились')
        self.value += 1
        return self.tasks[self.value]

    def __len__(self):
        return len(self.tasks)

    def __iter__(self):
        self.value = -1
        return self

todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')

for item in todo_list: print(item)
