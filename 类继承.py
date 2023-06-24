class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, gender):
        self.gender = gender
        super().__init__(name, age)  # 继承Person类的属性


stu1 = Student('Jack', 20, 'male')
stu1.info()
