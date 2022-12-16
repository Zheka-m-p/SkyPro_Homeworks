#class Post:
    #title = 'soon'
    #likes = 0
# Создание класса через type
Post = type('Post', (), {'title': 'soon', 'likes': 0})

class A:
    def show(self):
        print('show')

class B:
    pass

def disp(self):
    print(f"{self.title}, {self.likes}")

Post = type('Post', (A, B), {'title': 'soon', 'likes': 0, 'disp': disp})
p = Post()
print(p.likes)
p.show()
p.disp()
# добавление атрибутов через фукнцию
def create_class(name, based, attrs):
    attrs.update({'title': 'soon', 'likes': 0})
    return type(name, based, attrs)

class Post(metaclass=create_class):
    def show(self):
        print('show')

p = Post()
p.title
p.likes
# добавление или изменение атрибутов, методов через класс
class Meta(type):
    def __new__(cls, name, based, attrs):
        attrs.update({'title': 'soon', 'likes': 0, 'done': True})
        return type.__new__(cls, name, based, attrs)


class Post(metaclass=Meta):
    def show(self):
        print('show')

p = Post()
print(p.done, ' - is "done" atribut')
