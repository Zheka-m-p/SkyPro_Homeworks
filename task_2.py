from itertools import combinations


def search_count_substring(string):
    set_substing = set()
    count = len(string)  # сколько будем выдергивать из строки символов
    while string:
        data = list(combinations(string, count))
        for case in data:
            set_substing.add(''.join(case))
        count -= 1
        if count == 0:
            break
    return len(set_substing) + 1


assert search_count_substring('gfg') == 7
assert search_count_substring('ggg') == 4
assert search_count_substring('') == 1 # это уже работает как надо
