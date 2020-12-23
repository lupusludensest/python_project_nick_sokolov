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
        self.shoot = 0
        self.strike = 0
        self.doc_gave_health = 0

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

    def archer_shoot(self): # archer shoot
        self.shoot += 1

    def infantryman_strike(self): # infantryman strike
        self.strike += 1

    def gave_health(self): # gave health by doctor
        self.doc_gave_health += 1

    def get_health(self): # print out health
        return f'{self.name} health: {self.health}'

    def get_move(self): # print out move
        return f'{self.name} move: {self.move}'

    def get_shoot(self): # print out shoot/s by archer
        return f'{self.name} shoots: {self.shoot}'

    def get_strike(self): # print out strike/s by infantryman
        return f'{self.name} strikes: {self.strike}'

    def get_doc_gave_health(self): # print out health given by doctor
        return f'{self.name} gave health: {self.doc_gave_health}'

class Archer(Wariors):
    def tell_function(self):
        print(f'I am an archer!')

class Doctor(Wariors):
    def tell_function(self):
        print(f'I am a doctor!')

class Infantryman(Wariors):
    def tell_function(self):
        print(f'I am an infantryman!')

archer_1 = Archer("First archer")
doctor_1 = Doctor("First doctor")
infantryman_1 = Infantryman("First infantryman")

archer_1.say_name()
archer_1.tell_function()
archer_1.health_up()
archer_1.move_up()
archer_1.archer_shoot()
print(archer_1.get_health())
print(archer_1.get_move())
print(archer_1.get_shoot(), "\n")

doctor_1.say_name()
doctor_1.tell_function()
doctor_1.health_up()
doctor_1.health_up()
doctor_1.move_up()
doctor_1.move_up()
doctor_1.gave_health()
print(doctor_1.get_health())
print(doctor_1.get_move())
print(doctor_1.get_doc_gave_health(), "\n")

infantryman_1.say_name()
infantryman_1.tell_function()
infantryman_1.health_up()
infantryman_1.health_up()
infantryman_1.health_up()
infantryman_1.move_up()
infantryman_1.move_up()
infantryman_1.move_up()
infantryman_1.infantryman_strike()
print(infantryman_1.get_health())
print(infantryman_1.get_move())
print(infantryman_1.get_strike(), "\n")


