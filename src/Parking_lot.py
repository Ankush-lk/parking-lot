import sys
sys.path.append('/home/Srivamsi.s/PycharmProjects/parking-lot/src')
# from src.Vehicle import Vehicle as vehicle
from src.Vehicle import Car as car
import datetime


class Parking_lot:

    def __init__(self):
        self.size = 0
        self.lot_list = [0]*0
        self.occupied_count = -1
        # self.slotID = -1
        self.inTime = 0
        self.outTime = 0

    def create_parking_lot(self, size):
        self.size = size
        self.lot_list = [0]*size
        self.occupied_count = 0
        # self.slotID = -1
        self.inTime = 0
        self.outTime = 0

    def getVacantNo(self):
        return self.size - self.occupied_count

    def find_vacant_spot(self):
        for x in range(0, self.size):
            if self.lot_list[x] == 0:
                return x
        return -1

    def carParked(self, vehicle):
        if self.occupied_count < self.size:
            slotID = self.find_vacant_spot()
            self.occupied_count += 1
            self.lot_list[slotID] = car(vehicle.vehicleID, vehicle.colour)
            self.inTime = datetime.datetime.now()
            return slotID
        else:
            return -1

    def carCheckOut(self, slot):
        self.occupied_count -= 1
        self.lot_list[slot] = 0
        self.outTime = datetime.datetime.now()
        return "Car Checked out"

    def find_my_car(self, regno):
        if self.occupied_count == 0:
            return -1
        else:
            for x in range(0, self.size):
                try:
                    if self.lot_list[x].vehicleID == regno:
                        return x
                except AttributeError:
                        return "No vehicle found"


'''
lot = Parking_lot()
print(lot.lot_list)
lot.create_parking_lot(10)
print(lot.lot_list)

print('vehicle1')
v1 = vehicle('abcd1234', 'blue')
print(v1.vehicleID, v1.colour)

print(lot.getVacantNo())
print(lot.find_vacant_spot())
print(lot.carParked(v1))

print(lot.lot_list)

print(lot.find_my_car('abcd1234'))


print('vehicle2')
v2 = vehicle('2abcd1234', 'blue')
print(v2.vehicleID, v2.colour)
# lot = Parking_lot()
# print(lot.lot_list)
# lot.create_parking_lot(10)
print(lot.lot_list)

print(lot.getVacantNo())
print(lot.find_vacant_spot())
print(lot.carParked(v2))

print(lot.lot_list)

print(lot.find_my_car('2abcd1234'))

print('vehicle3')
v3 = vehicle('3abcd1234', 'blue')
print(v3.vehicleID, v3.colour)
# lot = Parking_lot()
# print(lot.lot_list)
# lot.create_parking_lot(10)
print(lot.lot_list)

print(lot.getVacantNo())
print(lot.find_vacant_spot())
print(lot.carParked(v3))

print(lot.lot_list)

print(lot.find_my_car('3abcd1234'))

print(lot.carCheckOut(1))
print(lot.lot_list)

'''