import src.Vehicle as vehicle
import datetime

class Parking_lot:

    def __init__(self, size):
        self.size = size
        self.lot_list = [0] * size
        self.occupied_count = -1
        self.slotID = -1
        self.inTime = 0
        self.outTime = 0

    def getVacantNo(self):
        return self.size - self.occupied_count

    def find_vacant_spot(self):
        for x in range(0, self.size):
            if self.lot_list[x] == -1:
                return x
            else:
                return -1

    def carParked(self, regno):
        if self.occupied_count < self.size:
            self.slotID = self.find_vacant_spot()
            self.occupied_count += 1
            self.lot_list[self.slotID] = vehicle.Car(regno)
            self.inTime = datetime.datetime.now()
            return self.slotID
        else:
            return -1

    def carCheckOut(self):
        self.occupied_count -= 1
        self.lot_list[self.slotID] = -1
        self.outTime = datetime.datetime.now()

    def find_my_car(self, regno):
        if self.occupied_count == 0:
            return -1
        else:
            for x in range(0,self.size):
                if self.lot_list[x] == regno:
                    return  x


