class Person(object):
    def __new__(cls, *args, **kwargs):
        print(f'__new__被调用,cls的id为:{id(cls)}')      # 3728
        obj = super().__new__(cls)
        print(f'创建对象obj的id为:{id(obj)}')     # 8704
        return obj

    def __init__(self, name):
        print(f'__init__被调用，self的id为:{id(self)}')       # 8704
        self.name = name


print(f'object类对象id为:{id(object)}')     # 2208
print(f'Person类对象id为:{id(Person)}')     # 3728

p = Person('Jack')
print(f'p这个实例化对象id为:{id(p)}')       # 8704
