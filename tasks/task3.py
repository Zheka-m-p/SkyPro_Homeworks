class Student:
    def __init__(self, name, stud_id):
        self.name = name
        self.stud_id = stud_id
        self.lap = self.Laptop()
        #self.brand = self.Laptop().brand
        #self.cpu = self.Laptop().cpu
        #self.ram = self.Laptop().ram

    def show(self):
        print(
            f"{self.name} {self.stud_id}\n{self.Laptop().brand} {self.Laptop().cpu} {self.Laptop().ram}")


    class Laptop:
        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i5'
            self.ram = 8


# Создаем двух студентов
s1 = Student('Ivan', 2)
s2 = Student('Mary', 3)

# Выводим данные по студенту и его нотбуку
s1.show()
#Ivan 2
#Hp i5 8
print()
# Увеличиваем память у ноутбука студента s1
s1.lap.ram = 16
s1.show()
#Ivan 2
#Hp i5 16
print()
# У каждого студента отдельный ноутбук (уникальный объект)
lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))
