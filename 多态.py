# 多态常用于继承上，即不同的子类相同的行为有不同的表现方法
# 通常父类不直接实现（抽象类），由子类来具体实现
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('汪汪汪!')


class Cat(Animal):
    def speak(self):
        print('喵喵喵~~')


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)
