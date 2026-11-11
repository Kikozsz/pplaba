from dataclasses import dataclass
from datetime import datetime, timedelta
#броньбилетырейсы
@dataclass
class Transport:
    id: int
    transport_type: str
    model: str
    capacity: int

@dataclass
class Trip:
    id: int
    transport: str
    departure_city: str
    arrival_city: str
    departure_time: datetime
    arrival_time: datetime
    price: int

@dataclass
class Booking:
    id: int
    passenger_name: str
    seat_number: int
    active: bool = True

#sistema br osnovnaya
@dataclass
class BookingSystem:
    def __init__(self):
        self.transports = {}
        self.trips = {}
        self.bookings = {}
        self.next_booking_id = {}

    def add_transport(self, transport):

    def add_trip():
    def show_trips(self):
        if self.trips:
            for trip in self.trips.values():
                transport = self.transports[trip.transport_id]
                print( f"\nРейс №{trip.id}: "
                      f"{trip.departure_city} -> {trip.arrival_city}")
                #trans
                #depar
                #arr
                #...
    def search_trips(self, departure, arrival, price):
        result = []
        for trip in self.trips#...
        return result
    
    def get_free_seats(self, trip_id):
        if trip_id not in self.trips:
            raise ValueError("Рейс не найден.")

        trip = self.trips[trip_id]
        transport = self.transports[trip.transport_id]

        occupied = set()
    def book_ticket():
    def cancel_booking(self, booking_id):
    def show_passenger_bookings(self, passenger_name):

def read_datetime(prompt):

def create_data(system):



def main():
    system = BookingSystem()
    create_data(system)
    while True