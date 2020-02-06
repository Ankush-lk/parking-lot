class Vehicle:
    def __init__(self, regNo):
        self.vehicleID = regNo


class Car(Vehicle):
    def __init__(self, regNo):
        Vehicle.__init__(regNo)

    def getType(self):
        return 'Car'