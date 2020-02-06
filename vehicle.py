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

    def get_vacant_count(self):
        return self.size - self.occupied_count

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

    def get_spot_details(self, spotID):
        data = {}
        vehicle = self.lot_list[spotID]
        data['vehicle_regNo'] = vehicle.regNo
        data['colour'] = vehicle.colour
        data['vehicle_type'] = vehicle.vehicle_type
        return data


# ticket_dict = dict()

class ticket_dict_class:

    def __init__(self):
        self.dictionary = {}
        pass

    def get_dictionary(self):
        return self.dictionary


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

    def get_ticketID(self):
        return self.ticketID

    def checkout(self, ticket_dict, lot_list):
        ticket = ticket_dict[str(self.ticketID)]
        ticket.checkoutTime = datetime.now()
        ticket_dict[self.ticketID] = ticket
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


ticket_dict_instance = ticket_dict_class()
ticket_dict = ticket_dict_instance.get_dictionary()

# ticket_dict = dict()

lot = parking_lot(10)


# lot_list = lot.get_parking_list


def assign_ticket(ticket_dict, lot, veh_colour, veh_regNo, veg_type):
    vehicle_object = Vehicle(veh_regNo, veh_colour, veg_type)
    empty_spotID = lot.find_empty_spot()
    lot.add_spot(empty_spotID, vehicle_object)
    ticket_object = Ticket(empty_spotID)
    add_ticket(ticket_object, ticket_dict)
    print("Ticket successfully created")
    print(ticket_object.get_all_values())
    print()
    return ticket_object


# print(add_vehicle(ticket_dict, lot, 'blue', 'qwer8465', '0'))
tick_obj = assign_ticket(ticket_dict, lot, 'blue', 'qwer8465', '0')
spotID_new_vehicle = tick_obj.spotID
print(lot.get_spot_details(spotID_new_vehicle))
# print(lot.lot_list)

print('---vehicle checkout---')
tick_obj.checkout(ticket_dict, lot.lot_list)
print(lot.lot_list)
