class Vehicle:
    def __init__(self, regNo, colour):
        self.vehicleID = regNo
        self.colour=colour


class Car(Vehicle):
    def __init__(self, regNo):
        Vehicle.__init__(regNo)

    def getType(self):
        return 'Car'