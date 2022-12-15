class MyList(list):
    def __init__(self, lst):
        self.lst = lst
        print('Работает магический метод')

    def __setitem__(self, key, value):
        print('Работает магический метод')        
        self.lst[key] = value

    def __getitem__(self, key):
        print('Работает магический метод')
        return self.lst[key]
        
    def __str__(self):
        print('Работает магический метод')
        return 'ffs'

    def __len__(self):
        print('Работает магический метод')
        return len(self.lst)
    
    def __eq__(self, value):
        print('Работает магический метод')
        return self.lst == value

lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))
