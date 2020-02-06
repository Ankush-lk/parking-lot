class Parking_lot:

    def __init__(self, size):
        self.size = size
        self.lot_list = [0] * size
        self.occupied_count = 0
        self.cur_spot = 0

    def getVacantNo(self):
        return self.size - self.occupied_count

    def find_vacant_spot(self, cur_spot):
        pass
