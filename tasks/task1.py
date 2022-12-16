def calc_salt(value):
    try:
        return value / 1000 * 10
    except TypeError:
        try:
            return int(value) / 1000 * 10
        except ValueError:
            print(f"invalid literal for int() with base 10: '{value}'")
            return 0.0


print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('abc'))
