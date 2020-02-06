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
        self.lot_list = [0] * size
        self.occupied_count = 0
        self.cur_spot = 0


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

    def get_slot_details(self, spotID):
        data = {}
        vehicle = self.lot_list[spotID]
        data['vehicle_regNo'] = vehicle.regNo
        data['colour'] = vehicle.colour
        data['vehicle_type'] = vehicle.vehicle_type
        return data


# ticket_dict = dict()

class ticket_dict_class:
    # dictionary = dict()

    def __init__(self):
        # self.dictionary = dict()
        pass

    def get_dictionary(self):
        return dict()


def add_ticket(ticket, ticket_dictionary):
    ticket_dictionary[str(ticket.ticketID)] = ticket


class Ticket:

    def __init__(self, spotID):
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

    def checkout(self, ticket_dict, lot_list):
        ticket = ticket_dict[str(self.ticketID)]
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


ticket_dict_instance = ticket_dict_class
ticket_dict = ticket_dict_instance.get_dictionary()

# ticket_dict = dict()

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
ticket1 = Ticket(empty_spotID)
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

ticket2 = Ticket(empty_spotID)
add_ticket(ticket2, ticket_dict)

print(ticket2.get_all_values())
ticketID = str(ticket2.get_ticketID())
print(ticket_dict[ticketID])

print('---vehicle 3---')
v3 = Vehicle('pqrs0987 clone', 'red', '3')

empty_spotID = lot.find_empty_spot()
lot.add_spot(empty_spotID, v3)
print(lot.lot_list)

ticket3 = Ticket(empty_spotID)
add_ticket(ticket3, ticket_dict)

print(ticket3.get_all_values())
ticketID = str(ticket3.get_ticketID())
print(ticket_dict[ticketID])

print('---vehicle2-checkout---')
ticket2.checkout(ticket_dict, lot.lot_list)
# print('abcde')
print(lot.lot_list)
print(lot.get_slot_details(0))


def add_vehicle(ticket_dict, veh_colour, veh_regNo, veg_type):
    vehicle_object = Vehicle(veh_regNo, veh_colour, veg_type)
    empty_spotID = lot.find_empty_spot()
    lot.add_spot(empty_spotID, vehicle_object)
    ticket_object = Ticket(empty_spotID)
    add_ticket(ticket_object, ticket_dict)
    print("Ticket successfully created")
    print(ticket_object.get_all_values())
    print()
    return ticket_object.ticketID


print(add_vehicle(ticket_dict, 'blue', 'qwer8465', '0'))
