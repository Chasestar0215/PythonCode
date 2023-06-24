import os

current_path = os.getcwd()
lst = os.listdir(current_path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

