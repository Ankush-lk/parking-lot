import uuid
from datetime import datetime


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

    def get_parking_list(self):
        return self.lot_list

    def add_spot(self, spotID, vehicle):
        # for i in range(0, 4):
        self.lot_list[spotID] = vehicle
        self.occupied_count += 1
        self.cur_spot += 1
        return self.lot_list

    def find_empty_spot(self, cur_spot=0):
        if self.lot_list[cur_spot] == 0:
            return cur_spot
        else:
            for i in range(len(self.lot_list)):
                if self.lot_list[i] == 0:
                    return i


# ticket_dict = dict()

class ticket_dict_class:
    def __init__(self):
        self.dictionary = dict()
        # pass

    def create_dict(self):
        return self.dictionary


def add_ticket(ticket, ticket_dictionary):
    ticket_dictionary[str(ticket.ticketID)] = ticket


class Ticket:

    def __init__(self, vehicle, spotID):
        self.ticketID = uuid.uuid4()
        self.checkinTime = datetime.now()
        self.checkoutTime = str()
        # self.vehicle_reg_no = vehicle.regNo
        # self.vehicle_type = vehicle.vehicle_type
        # self.vehicle_colour = vehicle.colour
        self.spotID = spotID

        # ticket_dict[self.ticketID] = vehicle.regNo

    # def create_ticket(self, vehicle, slotID, ticket_dict):
    #     self.vehicle_reg_no = vehicle.regNo
    #     self.vehicle_type = vehicle.vehicle_type
    #     self.vehicle_colour = vehicle.colour
    #     self.slotID = slotID
    #
    # return self.ticketID
    # def generate_ticket(self, ticket_dict):
    #     ticket_dict[self.ticketID] =

    def get_ticketID(self):
        return self.ticketID

    def checkout(self, ticketID, ticket_dict, lot_list):
        ticket = ticket_dict[ticketID]
        ticket.checkoutTime = datetime.now()
        ticket_dict[ticketID] = ticket
        spotID = ticket.spotID
        lot_list[spotID] = 0

    def get_all_values(self):
        data = {
                # 'ticketID': self.ticketID,
                'checkinTime': self.checkinTime,
                # 'vehicle_reg_no': self.vehicle_reg_no,
                # 'vehicle_type': self.vehicle_type,
                # 'vehicle_colour': self.vehicle_colour,
                'spotID': self.spotID
                }
        return data


ticket_dict = ticket_dict_class.create_dict()

lot = parking_lot(10)
l1 = lot.get_parking_list
print(lot.lot_list)
# print(lot.find_empty_spot())

print('---vehicle 1---')
v1 = Vehicle('abcd1234', 'blue', '4')
print(v1.colour)

empty_spotID = lot.find_empty_spot()
lot.add_spot(empty_spotID, v1)
print(lot.lot_list)

# ticket1 = Ticket().create_ticket(v1, empty_spotID, ticket_dict)
ticket1 = Ticket(v1, empty_spotID)
# ticket_dict = ticket_dict.create_dict()
# ticket_dict_class.add_ticket(ticket1, ticket_dict)
add_ticket(ticket1, ticket_dict)

# print('-----------')
print(ticket1.get_all_values())
# print('---')
ticketID = str(ticket1.get_ticketID())
print(ticket_dict[ticketID])

print('---vehicle 2---')
v2 = Vehicle('pqrs0987', 'red', '3')

empty_spotID = lot.find_empty_spot()
lot.add_spot(empty_spotID, v2)
print(lot.lot_list)

ticket2 = Ticket(v2, empty_spotID)
add_ticket(ticket2, ticket_dict)

print(ticket2.get_all_values())
ticketID = str(ticket2.get_ticketID())
print(ticket_dict[ticketID])

print('---vehicle 3---')
v3 = Vehicle('pqrs0987 clone', 'red', '3')

empty_spotID = lot.find_empty_spot()
lot.add_spot(empty_spotID, v3)
print(lot.lot_list)

ticket3 = Ticket(v3, empty_spotID)
add_ticket(ticket3, ticket_dict)

print(ticket3.get_all_values())
ticketID = str(ticket3.get_ticketID())
print(ticket_dict[ticketID])

print('---vehicle2-checkout---')
ticket3.checkout(ticket2.spotID, ticket_dict, l1)

print(l1)
