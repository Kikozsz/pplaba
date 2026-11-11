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
    : str
    : str
    : str
    : datetime
    : datetime
    : int
@dataclass
class Booking:

#sistema br osnovnaya
@dataclass
class BookingSystem:
    def __init__(self):
        self.transports = {}
        self.trips = {}
        self.bookings = {}
        self.next_booking_id = {}