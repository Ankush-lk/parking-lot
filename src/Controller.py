from src.Parking_lot import Parking_lot as park
from src.Vehicle import Car
from src.Tickets import Tickets
# import sys
# sys.append('/home/Srivamsi.s/PycharmProjects/parking-lot/src')

class Controller:
    def __init__(self):
        self.lot = park()
        self.ticket_obj = Tickets()
        print('controller initialized')

    def create_vehicle(self, regno, colour):
        print("vehicle regNO: {} |  colour: {}".format(regno, colour))
        return Car(regno, colour)

    def create_lot(self, size):
        print("lot size: {}".format(size))
        self.lot.create_parking_lot(size)

    def create_ticket(self, vehicle):
        lot = self.lot
        ticketID = self.ticket_obj.raise_ticket(vehicle, lot)
        print("ticket created {}".format(self.ticket_obj.ticket_dict.keys()))
        return ticketID

    def delete_ticket(self, ticketID):
        print("ticketID {} deleted".format(ticketID))
        lot = self.lot
        self.ticket_obj.close_ticket(ticketID, lot)

    def get_vehicle_details(self, vehicle):
        data = {}
        data['vehicleID'] = vehicle.vehicleID
        data['colour'] = vehicle.colour
        print(data)

    def get_vacancy_count(self):
        print('Vacancy count', self.lot.getVacantNo())


if __name__ == '__main__':
    c= Controller()
    c.create_lot(10)
    v1 = c.create_vehicle('abcd123', 'red')

    ticketID = c.create_ticket(v1)
    c.get_vacancy_count()
    c.delete_ticket(ticketID)
    c.get_vehicle_details(v1)
    c.get_vacancy_count()


