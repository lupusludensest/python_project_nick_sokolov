# -*- coding: utf-8 -*-

class Engine:
    def move(self):
        print(f'I move')

    def stop(self):
        print(f'I stopped')

class Camera:
    def look(self):
        print(f'I watch')

class Cleaner:
    def clean(self):
        print(f'I am cleaning')

class MyDevice(Engine, Camera):
    def __init__(self, name):
        self.name = name
        print(f'Hi, {self.name}')

class Vacoom(Engine, Cleaner, Camera):
    def __init__(self, name):
        self.name = name
        print(f'Hi, {self.name}')

robot1 = MyDevice(f'Valley')
robot1.move()
robot1.stop()
robot1.look()

robot2 = Vacoom(f'R2D2')
robot2.move()
robot2.stop()
robot2.look()
robot2.clean()


