from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, country, price):
        super().__init__(make, model, country)
        self.price = price

class Plane(Vehicle):
    def __init__(self, make, model, country, number_of_seats):
        super().__init__(make, model, country)
        self.number_of_seats = number_of_seats

class Boat(Vehicle):
    def __init__(self, make, model, country, sail_boat):
        super().__init__(make, model, country)
        self.sail_boat = sail_boat

class RaceCar(Car):
    def __init__(self, make, model, country, price, max_speed):
        super().__init__(make, model, country, price)
        self.max_speed = max_speed

nissan_tiida = Car("Nissan", "Tiida", "Japan","5000")
boing_777 = Plane("Boing", "777", "USA", 273)
bavaria_30 = Boat("Bavaria", "30", "Germany", "Yes")
ferrari_enzo = RaceCar("Ferrari", "Enzo", "Italy", "3.300.000$",510)

print(nissan_tiida)
print(boing_777)
print(bavaria_30)
print(ferrari_enzo)
