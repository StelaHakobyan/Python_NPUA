class Vehicle:
    def __init__(self, make, model, country):
        self.make = make
        self.model = model
        self.country = country

    def __str__(self):
        return f"{self.make} {self.model} {self.country}"