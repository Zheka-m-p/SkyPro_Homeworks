def get_val(collection, key, default=None):
    """Возвращает значение по ключу из словаря, иначе возвращает переданное значение по умолчанию"""
    return collection.setdefault(key, default)


def set_(collection, path, value):
    """Меняет значение по указанному пути, если нет, то создаёт этот путь и новое значение для него.
       Функция ничего не возвращает!"""

    end = len(path)
    for i in range(end):
        if i == end - 1:
            collection[path[i]] = value
        if path[i] not in collection:
            collection[path[i]] = {}
            return set_(collection[path[i]], path[1:], value)
        else:
            return set_(collection[path[i]], path[1:], value)

