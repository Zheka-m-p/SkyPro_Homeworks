import os

class ChangeDir:
    def __init__(self, dir_name):
        #print('__init__')
        self.dir_name = dir_name


    def __enter__(self):
        #print('__enter__')
        os.chdir(self.dir_name)

    def __exit__(self, ex_type, ex_val, ex_tb):
        #print('__exit__')
        os.chdir('../')


with ChangeDir('dir1'):
    print(os.listdir())

with ChangeDir('dir2'):
    print(os.listdir())
