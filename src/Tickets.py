import uuid
# import src.Parking_lot as park
from src.Parking_lot import Parking_lot as park
from src.Vehicle import Car as car


class Tickets:
    def __init__(self):
        self.park = park()
        self.ticketID = -1
        self.flag = 0
        self.ticket_dict = {}
        self.success = False

    # def raise_ticket(self, size, regno):
    def raise_ticket(self, vehicle, lot):
        # if self.flag == 0:
        #     park.create_parking_lot(size)
        #     flag = 1
        slot = lot.carParked(vehicle)
        if slot != -1:
            self.ticketID = uuid.uuid4()
            self.ticket_dict[self.ticketID] = slot
            self.success = True
        if self.success:
            return self.ticketID
        else:
            return -1

    def close_ticket(self, ticketID, lot):
        slot = self.ticket_dict[ticketID]
        lot.carCheckOut(slot)
        try:
            del self.ticket_dict[ticketID]
        except KeyError:
            raise KeyError('Key not found')

    # def remove_parking_lot(self):
    #     self.flag = 0


'''
v1 = car('abcd1234', 'red')
lot = park()
# lot = park.create_parking_lot(10)
lot.create_parking_lot(10)


ticket = Tickets()
ticketID = ticket.raise_ticket(v1, lot)
print(lot.lot_list)
print(ticket.ticket_dict[ticketID])
ticket.close_ticket(ticketID, lot)
print(ticket.ticket_dict)
print(lot.lot_list)

'''
