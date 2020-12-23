# Домашка к уроку 2.
# Представим, что мы разрабатываем игру и нам нужно создать несколько типов персонажей:
# лучник, медик и пехотинец. Каждый обладает уникальными свойствами,
# первый умеет поражать цели на дистанции,
# второй восстанавливать здоровье свое и других персонажей,
# третий может сражаться только в ближнем бою.
# Разумеется всех троих объединяют некоторые параметры,
# все имеют объем здоровья,
# умеют перемещаться(достаточно просто выводить сообщение об этом),
# терять и прибавлять здоровье.
# Задача, реализовать описание выше в ООП код на python.

class Wariors():
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.move = 0

    def say_name(self): # say name
        print(self.name)

    def health_up(self): # health up
        self.health += 1

    def health_down(self): # healt down
        self.health -= 1

    def move_up(self): # move up
        self.move += 1

    def move_down(self): # move down
        self.move -= 1

    def get_health(self): # print out health
        return f'{self.name} health: {self.health}'

    def get_move(self): # print out move
        return f'{self.name} move: {self.move}'

