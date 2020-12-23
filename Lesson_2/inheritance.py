# Решение проблемы переопределения
# метода __init__() при
# множественном наследовании

class Class1:
    def __init__(self):
        super().__init__()
        self.p1 = "p1 from class1"

    def get_p1(self):
        return self.p1

class Class2:
    def __init__(self):
        super().__init__()
        self.p2 = "p2 from class2"

    def get_p2(self):
        return self.p2

class Class3(Class1, Class2):
    pass

a = Class3()
print(a.get_p1())
print(a.get_p2())