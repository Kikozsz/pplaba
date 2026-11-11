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