class Vehicle:
    def __init__(self, regNo, colour):
        self.regNo = regNo
        self.colour=colour


class Car(Vehicle):
    def __init__(self, regNo, colour):
        # Vehicle.__init__(regNo, colour)
        super(Car, self).__init__(regNo, colour)
        
    def getType(self):
        return 'Car'



# v1 = Vehicle('abcd1234', 'blue')
# print(v1.colour, v1.vehicleID)
# c1 = Car(v1.vehicleID, v1.colour)
# print(c1.colour,c1.vehicleID,c1.getType())