import os

current_path = os.getcwd()
lst = os.walk(current_path)
for dirpath, dirname, filename in lst:
    print(dirpath)
    print(dirname)
    print(filename)
    print('------------')
