class Transport():
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.noise = 0

    def say_name(self):
        print(self.name)

    def speed_up(self):
        self.speed += 1
        self.noise += 0.2

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        try:
            self.noise = noise
            return True
        except BaseException:
            return False

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        try:
            self.speed = speed
            return True
        except BaseException:
            return False

