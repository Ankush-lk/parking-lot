import uuid
import datetime

class Vehicle:
    def __init__(self, regNo, colour, vehicle_type):
        self.regNo = regNo
        self.colour = colour
        self.vehicle_type = vehicle_type


class parking_lot:

    def __init__(self, size):
        self.size = size
        self.lot_list = [0]*size
        self.occupied_count = 0
        self.cur_spot = 0

        # pass

    # def create_lot(self, size):
    #     pass

    # def get_vacant_count(self):

    def add_spot(self, spotID):
        # for i in range(0, 4):
        self.lot_list[spotID] = 1
        return self.lot_list

    def find_empty_spot(self, cur_spot):
        if self.lot_list[cur_spot] == 0:
            return cur_spot
        else:
            for i in range(len(self.lot_list)):
                if self.lot_list[i] == 0:
                    return i


# ticket_dict = dict()

class ticket_dict:
    def __init__(self):
        pass

    def create_dict(self):
        return dict()

class Ticket(ticket_dict):


    def __init__(self):
        self.ticketID = uuid.uuid4()
        self.checkinTime = datetime.now()


    def create_ticket(self, vehicle):
        self.vehicle_reg_no = vehicle.regNo
        self.vehicle_type = vehicle.vehicle_type
        self.vehicle_colour = vehicle.colour
        ticket_dict[self.ticketID] = vehicle.regNo
        return self.ticketID

    def checkout(self, ticketID):

        ticket = ticket_dict[ticketID]
        ticket.checkoutTime = datetime.now()
        ticket_dict[ticketID] = ticket


lot = parking_lot(10)
lot.add_spot()
print(lot.lot_list)
print(lot.find_empty_spot())
v1 = Vehicle('abcd1234', 'blue', '4')
print(v1)
ticket1 = Ticket()