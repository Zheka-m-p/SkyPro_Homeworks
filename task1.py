# 1)
import re


def to_camel_case(text):
    return ''.join(word.title() for word in re.split('_|-', text))


assert to_camel_case('----python-text_best-world') == 'PythonTextBestWorld'


# 2)
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# 3
count_bits = lambda n: bin(n).count('1')
assert count_bits(15) == 4


# 4
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


assert digital_root(128) == 2
assert digital_root(1569) == 3
# 5
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"

assert even_or_odd(10) == "Even"
assert even_or_odd(11) == "Odd"
