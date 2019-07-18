# Inheritance Polymorphism
# Method overriding


class LandVehicle:
    def __init__(self, num_of_wheels, colour, owner):
        self.num_of_wheels = num_of_wheels
        self.colour = colour
        self.owner = owner

    def honk(self):
        return 'HORN NOISE'


class Car(LandVehicle):
    def __init__(self, colour, owner):
        super().__init__(4, colour, owner)

    def honk(self):
        return 'Beep Beep'


class Lorry(LandVehicle):
    def __init__(self, num_of_wheels, colour, owner, cargo):
        super().__init__(4, colour, owner)
        self.cargo = cargo

    def honk(self):
        return 'HOOOOOOOOOOOOOOOOOOOOOOOOOONK HOOOOOOOOOOONK'


class Bicycle(LandVehicle):
    def __init__(self, colour, owner):
        super().__init__(2, colour, owner)

    def honk(self):
        return 'bring bring'


my_car = Car('Red', 'Hamza')
my_lorry = Lorry(18, 'Blue', 'Mujeebullah', 'Laptops')
my_bike = Bicycle('Green', 'Matt')

for horn in (my_car, my_lorry, my_bike):
    print(horn.honk())