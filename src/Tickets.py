import uuid
from src.Parking_lot import Parking_lot as park


class Tickets:
    def __init__(self):
        self.park = park()
        self.ticketID = -1
        self.flag = 0
        self.lot_dict = {}
        self.success = False

    def raise_ticket(self, size, regno):
        if self.flag == 0:
            park.create_parking_lot(size)
            flag = 1
        slot = park.carParked(regno)
        if slot != -1:
            self.ticketID = uuid.uuid4()
            self.lot_dict[self.ticketID] = slot
            self.success = True
        if self.success:
            return self.ticketID
        else:
            return -1

    def close_ticket(self, ticketID):
        slot = self.lot_dict.get(ticketID)
        park.Parking_lot.carCheckOut(slot)
        del self.lot_dict[ticketID]

    def remove_parking_lot(self):
        self.flag = 0

ticket = Tickets()
ticket.raise_ticket(10,1)