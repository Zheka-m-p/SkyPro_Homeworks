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
        return bool(self.__content)


todo_list = []

todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))

non_empty_tasks = [item for item in todo_list if item]
non_empty_tasks
len([item for item in todo_list if not item])
