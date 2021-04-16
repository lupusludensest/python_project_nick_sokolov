class Car:
    def __init__(self, brand, model, year, max_capacity):
        self.brand = brand
        self.model = model
        self.year = year
        self.max_capacity = max_capacity
        self.trunk = []

    def start_moving(self):
        return print(f"the {self.year} {self.brand} {self.model} starts moving")

    def stop_moving(self):
        return print(f"the {self.year} {self.brand} {self.model} stops moving")

    def check_trunk(self):
        return len(self.trunk)

    def add_to_trunk(self, something):
        if (self.check_trunk()+1) < self.max_capacity:
            message = f"{something} was put in the trunk of the {self.year} {self.brand} {self.model}."
            self.trunk.append(something)
        elif (self.check_trunk()+1) == self.max_capacity:
            message = f"{something} was put in the trunk of the {self.year} {self.brand} {self.model}, but there is no more space!"
            self.trunk.append(something)
        elif (self.check_trunk()+1) > self.max_capacity:
            message = f"There is no more space in the {self.year} {self.brand} {self.model} trunk!!!"
        return print(message)

car1 = Car("Nissa", "Altima", 2020, 5)
car1.start_moving()
car1.stop_moving()
car1.add_to_trunk("spare wheel")
car1.add_to_trunk("bag")
car1.add_to_trunk("ball")
car1.add_to_trunk("pump")
car1.add_to_trunk("swimming suit")
car1.add_to_trunk("bottle of water")
print(car1.check_trunk())
