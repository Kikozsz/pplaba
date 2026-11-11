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
    transport: int
    departure_city: str
    arrival_city: str
    departure_time: datetime
    arrival_time: datetime
    price: float

@dataclass
class Booking:
    id: int
    trip_id: int
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
        if transport.capacity < 0:
            raise ValueError("Количество мест должно быть больше нуля.")
        if tansport.id in self.transports:
            raise ValueError("Такой транспорт уже существует.")
        self.transports[transport.id] = transport

    def add_trip():
    def show_trips(self):
        if self.trips:
            for trip in self.trips.values():
                transport = self.transports[trip.transport_id]
                print( f"\nРейс №{trip.id}: "
                      f"{trip.departure_city} -> {trip.arrival_city}")
                print(f"Транспорт: {transport.transport_type} {transport.model}")
            print(f"Отправление: {trip.departure_time}")
            print(f"Прибытие: {trip.arrival_time}")
            print(f"Цена: {trip.price} руб.")
    def search_trips(self, departure, arrival):
        result = []
        for trip in self.trips.values():
            if(trip.departure_city.lower() == departure.strip().lower() and trip.arrival_city.lower() == arrival.strip().lower() and trip.departure_time > datetime.now()):
                result.append(trip)
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
    while True:
        print("\n========== БРОНИРОВАНИЕ БИЛЕТОВ ==========")
        print("1. Показать все рейсы")
        print("2. Найти рейсы")
        print("3. Забронировать билет")
        print("4. Отменить бронирование")
        print("5. Бронирования пассажира")
        print("6. Свободные места")
        print("7. Добавить транспорт")
        print("8. Добавить рейс")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        try:
            if choice == "1":
                system.show_trips()

            elif choice == "2":
                departure = input("Город отправления: ")
                arrival = input("Город прибытия: ")

                trips = system.search_trips(departure, arrival)
                if not trips:
                    print("Рейсы не найдены.")

                for trip in trips:
                    print(
                        f"Рейс №{trip.id}: "
                        f"{trip.departure_city} -> {trip.arrival_city}"
                    )