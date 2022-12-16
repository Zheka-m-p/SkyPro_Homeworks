class Meta(type):
    # Метакласс, чтобы в другом классе все атрибуты класса стали состо9ть из заглавных букв
    def __new__(cls, name, based, attrs):
        new_attrs = {}
        for k, v in attrs.items():
            if v != 'Math' and v != '__main__':
                new_attrs[k.upper()] = v
        new_1_attrs = {}
        new_1_attrs['__module__'] = '__main__'
        new_1_attrs['__qualname__'] = 'Math'
        # new_1_attrs['__qualname__'] = str(cls) # в общем виде хз как(
        new_attrs.update(new_1_attrs)
        return type.__new__(cls, name, based, new_attrs)


class Math(metaclass=Meta):
    pi = 3.141592653589793
    e = 2.718281828459045
    tau = 6.283185307179586

m = Math()
print(m.PI)
# 3.141592653589793
print(m.E)
# 2.718281828459045
print(m.pi)
# AttributeError: 'Math' object has no attribute 'pi'
