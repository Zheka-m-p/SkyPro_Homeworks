class TeamIterator:
    def __init__(self, team):
        self.team = team
        self.index = 0

    def __next__(self):

        if self.index < (len(self.team._juniorMembers) + len(self.team._seniorMembers)):
            if self.index < len(self.team._juniorMembers):
                result = (self.team._juniorMembers[self.index], 'junior')
            else:
                result = (self.team._seniorMembers[self.index - len(self.team._juniorMembers)], 'senior')
            self.index += 1
            return result
        else:
            raise StopIteration


class Team:
    """
    Хранит список джунов и синьоров, а также переопределяет метод __iter__().
    """

    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __iter__(self):
        """ Возвращает объект-итератор """
        return TeamIterator(self)


def main():
    # создаем команду
    team = Team()
    # добавляем имена джунов
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    # добавляем имена синьоров
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])

    print('*** Итерируемся по команде в цикле for ***')
    for member in team:
        print(member)

    print('*** Итерируемся по команде в цикле while ***')
    # Получаем итератор из итерируемого объекта - экземпляра класса Team
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
