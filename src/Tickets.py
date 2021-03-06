import uuid
import src.Parking_lot as park


class Tickets:
    def __init__(self):
        self.park = park()
        self.ticketID = -1
        self.flag = 0
        self.lot_dict = {}
        self.success = False

    def raise_ticket(self, size, regno):
        if self.flag == 0:
            park.Parking_lot.create_parking_lot(size)
            flag = 1
        slot = park.Parking_lot.carParked(regno)
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
        try:
            del self.ticket_dict[ticketID]
        except KeyError:
            raise KeyError('Key not found')

    def remove_parking_lot(self):
        self.flag = 0
