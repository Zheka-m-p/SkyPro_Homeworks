class Vehicle:

    def __init__(self, position):  # position: кортеж (10, 20)
        self.position = position

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    @staticmethod
    def calculate_route(source, to):
        return 0  # to be realized

    def move_along(self, route):
        print("moving")


class Mixsin:
    def turn_on_radio(self, value):
        print(f"Playing {value}")


class Car(Vehicle, Mixsin):
    pass


class Airplane(Vehicle):
    pass


car = Car((10, 20))
car.turn_on_radio('Moscow FM')
# Playing Moscow FM
car.position
air = Airplane((100, 3500))
# air.turn_on_radio
# AttributeError: 'Airplane' object has no attribute 'turn_on_radio'
