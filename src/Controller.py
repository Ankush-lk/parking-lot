from src.Parking_lot import Parking_lot as park
from src.Vehicle import Car
from src.Tickets import Tickets


class Controller:
    def __init__(self):
        self.lot = park()
        self.ticket_obj = Tickets()

    def create_vehicle(self, regno, colour):
        return Car(regno, colour)

    def create_lot(self, size):
        self.lot.create_parking_lot(size)

    def create_ticket(self, vehicle, lot):
        lot = self.lot
        self.ticket_obj.raise_ticket(vehicle, lot)

    def delete_ticket(self, ticketID, lot):
        lot = self.lot
        self.ticket_obj.close_ticket(ticketID, lot)

    def get_vehicle_details(self, vehicle):
        data = {}
        data['vehicleID'] = vehicle.vehicleID
        data['colour'] = vehicle.colour
        print(data)

    def get_vacancy_count(self):
        print('Vacancy count', self.lot.getVacantNo())




