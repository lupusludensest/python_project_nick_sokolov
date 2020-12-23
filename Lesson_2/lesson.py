from general import *

class Ship(Transport):
    def swim(self):
        print("I can swim")

class Aircraft(Transport):
    def fly(self):
        print("I can fly")

    def speed_up(self):
        self.speed += 5
        self.noise += 2

boat = Ship("Speedboat")
boat2 = Ship("Nameboat")
plane = Aircraft("Boeing")

boat.say_name()
boat2.say_name()
plane.say_name()

print(plane.get_speed(), plane.get_noise())
plane.speed_up()
print(plane.get_speed(), plane.get_noise())
plane.speed_up()
print(plane.get_speed(), plane.get_noise())
plane.speed_up()
print(plane.get_speed(), plane.get_noise())
plane.set_speed(100)
print(plane.get_speed(), plane.get_noise())


