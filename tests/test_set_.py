from skypro_day_20.two_func import set_


def testing_set():
    """Тестирование работы функции set_"""
    coll = {"a": {"b": {"c": 3}}}
    set_(coll, ["a", "b", "c"], 4)
    assert coll == {'a': {'b': {'c': 4}}}
    set_(coll, ['x', 'y', 'z'], 5)
    assert coll == {'a': {'b': {'c': 4}}, 'x': {'y': {'z': 5}}}
    set_(coll, ['a', 'b', 'm'], 'работает')
    assert coll == {'a': {'b': {'c': 4, 'm': 'работает'}}, 'x': {'y': {'z': 5}}}