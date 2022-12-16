class ReadItems:
    def __init__(self, file, mode):
        print('__init__')
        self.file = file
        self.mode = mode

    def __enter__(self):
        print('__enter__')
        self.f = open(self.file, self.mode)
        len_rows = len(list(self.f))
        self.f = open(self.file, self.mode)
        a, b, c = self.f.readline().strip().split(',')
        res = []
        for i in range(len_rows - 1):
            a_1, b_1, c_1 = self.f.readline().strip().split(',')
            res.append({a: a_1, b: b_1, c: c_1})
        return res
        
    def __exit__(self, ex_type, ex_val, ex_tb):
        print('__exit__')
        self.f.close()


def show_items(file):
    with ReadItems(file, 'r') as items:
        for item in items:
            print(item)


show_items('items.csv')
# вывод в консоль
#{'name': 'Phone', 'price': '100', 'quantity': '1'}
#{'name': 'Laptop', 'price': '1000', 'quantity': '3'}
#{'name': 'Cable', 'price': '10', 'quantity': '5'}
#{'name': 'Mouse', 'price': '50', 'quantity': '5'}
#{'name': 'Keyboard', 'price': '74.90', 'quantity': '5'}
