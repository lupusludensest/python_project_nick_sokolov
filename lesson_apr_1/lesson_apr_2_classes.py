# -*- coding: utf-8 -*-

class Human:
    def __init__(self, name, gender): # self указатель на экземпляр класса
        self.human_name = name
        self.human_gender = gender
        self.bag = []
        print(f'Human has been born, {self.human_name}, {gender}')

    def move(self):
        print(f'{self.human_name} goes')

    def put_to_bag(self, item):
        self.bag.append(item)
        print(f'{self.human_name} puts into the bag {item}')
        return len(self.bag)

    def get_bag(self):
        return len(self.bag), self.bag

    def __str__(self):
        return f'Human {self.human_name}'

    # __repr__ используется при вызове в списках
    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.bag)

    def __add__(self, other):
        return list(self.bag) + list(other.bag)

class Car():
    def __init__(self):
        self.passangers = []

    def add_passangers(self, passanger):
        self.passangers.append(passanger)


h1 = Human(f'Vasya', f'male')
h2 = Human(f'Masha', f'female')

print(len(h2), h2)

# print(h1.human_name)
# print(h1.human_gender)
#
# print(h2.human_name)
# print(h2.human_gender)
#
# h2.bag.append('Candy')
# h2.bag.append('Water')
h2.put_to_bag('Hamburger')
h2.put_to_bag('Candy')
h2.put_to_bag('Bread')
sum_bags = h1 + h2
print(sum_bags)
#
# print(len(h2), h2)

#
# h2.move()
#
# for i in h2.bag:
#     print(i)
#
# h2.move()
# for i in h2.get_bag():
#     print(i)

car1 = Car()
car1.add_passangers(h1)
car1.add_passangers(h2)
print("===")
print(car1.add_passangers(h1))