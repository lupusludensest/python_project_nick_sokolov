# -*- coding: utf-8 -*-

"""
def my_func(arg):
    try:
        return 10 + arg
    except BaseException as err:
        print(f'Got an error,\n{err}')
        return 0

print(my_func(10))
print(my_func(5))

print(my_func('text '))
"""

# Inheritance
class Animal:
    def move(self):
        print("It runs")

    def seat(self):
        print("It seats")

class Cat(Animal):
    def voice(self):
        print("It tells miawww")

class Dog(Animal):
    def voice(self):
        print("It tells gawww")

cat1 = Cat() # Inherited everithing from Animal and Cat
cat1.seat()
cat1.move()
cat1.voice()

dog1 = Dog() # Inherited everithing from Animal and Cat
dog1.seat()
dog1.move()
dog1.voice()