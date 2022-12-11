from skypro_day_20.two_func import get_val


def testing_get_val():
    """Тестирование работы функции get_val"""
    assert get_val({"hello": "world"}, "hello") == 'world'
    assert get_val({"hello": "world"}, "hello", "python") == 'world'
    assert get_val({}, "hello", "python") == 'python'
    assert get_val({}, 'pyhton') == None
