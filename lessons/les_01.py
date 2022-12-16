class Readfile:
    def __init__(self, file, mode):
        print('__init__')
        self.file = file
        self.mode = mode
        
    def __enter__(self):
        print('__enter__')
        self.f = open(self.file, self.mode)
        return self.f

    def __exit__(self, ex_type, ex_val, ex_tb):
        print('__exit__')
        self.f.close()

with Readfile('sample.txt', 'r') as f:
    print('some code')
    text = f.read()
    print(text)
    
