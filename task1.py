class Person:
    min_weight = 25.0
    min_age = 14
    max_age = 150

    @classmethod
    def verify_weight(cls, check_weight):
        if not isinstance(check_weight, float) or check_weight < cls.min_weight:
            raise ValueError('Вес должен быть вещественным числом от 25 и выше')
        return True

    @classmethod
    def verify_age(cls, check_age):
        if not isinstance(check_age, int) or check_age < cls.min_age or check_age > cls.max_age:
            raise ValueError('Возраст должен быть целым числом от 14 до 150')
        return True

    @classmethod
    def verify_passport(cls, check_passport):
        if isinstance(check_passport, str):
            if len(check_passport.split()) == 2:
                passport_1, passport_2 = check_passport.split()
                if len(passport_1) == 4 and len(passport_2) == 6:
                    if passport_1.isdigit() and passport_2.isdigit():
                        return True
                    else:
                        raise ValueError('Серия и номер паспорта должны содержать только числа')
                else:
                    raise ValueError('Неверный формат паспорта')
            else:
                raise ValueError('Неверный формат паспорта')
        else:
            raise ValueError('Паспорт должен быть строкой')
        # return True

    @classmethod
    def verify_fio(cls, check_fio):
        if isinstance(check_fio, str):
            if len(check_fio.split()) == 3:
                family_name, name, patronymic = check_fio.split()
                cheking_fio_all = [family_name, name, patronymic]
                if all([x for x in cheking_fio_all]):
                    if any(any(x.isdigit() for x in y) for y in cheking_fio_all):
                        raise ValueError('В ФИО можно использовать только буквенные символы')
                    else:
                        return True
                else:
                    raise ValueError('В фамилии, имени и отчестве должен быть хотя бы один символ')
            else:
                raise ValueError('Неверный формат записи ФИО')
        else:
            raise ValueError('ФИО должно быть строкой')

    def __init__(self, fio, age, passport, weight):
        self.__fio = fio
        if self.verify_age(age):
            self.__age = age
        if self.verify_passport(passport):
            self.__passport = passport
        if self.verify_weight(weight):  # Не понял, почему тут не надо ничего кроме веса
            self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        if self.verify_weight(new_weight):
            self.__weight = new_weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if self.verify_age(new_age):
            self.__age = new_age

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, new_passport):
        if self.verify_passport(new_passport):
            self.__passport = new_passport

    @property
    def fio(self):
        return self.__age

    @fio.setter
    def fio(self, new_fio):
        if self.verify_fio(new_fio):
            self.__fio = new_fio


p = Person('Иванов Иван Иванович', 50, '0000 000000', 85.0)
p.old = 100
p.passport = '1122 333444'
p.weight = 75.0
p.fio = 'Черников Евгений Викторович'
