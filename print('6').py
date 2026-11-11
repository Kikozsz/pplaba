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
        if transport.capacity <= 0:
            raise ValueError("Количество мест должно быть больше нуля.")
        if tansport.id in self.transports:
            raise ValueError("Такой транспорт уже существует.")
        self.transports[transport.id] = transport

    def add_trip(self, trip):
        if trip.transport_id not in self.transports:
            raise ValueError("Транспорт не найден.")

        if trip.departure_city.lower() == trip.arrival_city.lower():
            raise ValueError("Города должны отличаться.")

        if trip.departure_time <= datetime.now():
            raise ValueError("Дата отправления должна быть в будущем.")

        if trip.arrival_time <= trip.departure_time:
            raise ValueError("Дата прибытия должна быть позже отправления.")
        if trip.price < 0:
            raise ValueError("Цена не может быть отрицательной.")

        if trip.id in self.trips:
            raise ValueError("Такой рейс уже существует.")

        self.trips[trip.id] = trip

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
    def book_ticket(self, trip_id, passenger_name, seat_number):
        if trip_id not in self.trips:
            raise ValueError("Рейс не найден.")

        trip = self.trips[trip_id]
        transport = self.transports[trip.transport_id]

        if trip.departure_time <= datetime.now():
            raise ValueError("Рейс уже отправился.")

        if not passenger_name.strip():
            raise ValueError("Введите имя пассажира.")
        
        if not 1 <= seat_number <= transport.capacity:
            raise ValueError("Некорректный номер места.")

        if seat_number not in self.get_free_seats(trip_id):
            raise ValueError("Это место уже занято.")

        booking = Booking(
            self.next_booking_id,
            trip_id,
            passenger_name.strip(),
            seat_number
        )

        self.bookings[booking.id] = booking
        self.next_booking_id += 1

        return booking
    
    def cancel_booking(self, booking_id):
         if booking_id not in self.bookings:
            raise ValueError("Бронирование не найдено.")

        booking = self.bookings[booking_id]

    if not booking.active:
            raise ValueError("Бронирование уже отменено.")

        booking.active = True
    
    def show_passenger_bookings(self, passenger_name):
        found = False

        for booking in self.bookings.values():
            if booking.passenger_name.lower() == passenger_name.strip().lower():
                status = "Активно" if booking.active else "Отменено"

                print(
                    f"\nБронирование №{booking.id}"
                    f"\nРейс №{booking.trip_id}"
                    f"\nМесто: {booking.seat_number}"
                    f"\nСтатус: {status}"
                )

                found = True

        if not found:
            print("Бронирования не найдены.")

def read_datetime(prompt):
    print("Формат: ГГГГ-ММ-ДД ЧЧ:ММ")
    return datetime.strptime(input(prompt), "%Y-%m-%d %H:%M")

def create_data(system):
    system.add_transport(
        Transport(1, "Автобус", "Mercedes-Benz", 40)
    )
    system.add_transport(
        Transport(2, "Поезд", "Ласточка", 100)
    )
    system.add_transport(
        Transport(3, "Самолёт", "Airbus A320", 150)
    )
    tomorrow = datetime.now() + timedelta(days=1)
    system.add_trip(
        Trip(
            1, 1, "Москва", "Санкт-Петербург",
            tomorrow.replace(hour=8, minute=0),
            tomorrow.replace(hour=13, minute=0),
            1800.0
        )

    )
     system.add_trip(
        Trip(
            2, 2, "Москва", "Казань",
            tomorrow.replace(hour=10, minute=0),
            tomorrow.replace(hour=21, minute=0),
            2500.0
        )
    )

    system.add_trip(
        Trip(
            3, 3, "Москва", "Сочи",
            tomorrow.replace(hour=9, minute=30),
            tomorrow.replace(hour=12, minute=0),
            6500.0
        )
    )

     system.add_trip(
        Trip(
            4, 1, "Казань", "Самара",
            tomorrow.replace(hour=14, minute=0),
            tomorrow.replace(hour=18, minute=0),
            1200.0
        )
    )

    system.add_trip(
        Trip(
            5, 2, "Санкт-Петербург", "Москва",
            tomorrow.replace(hour=16, minute=0),
            tomorrow.replace(hour=22, minute=0),
            2200.0
        )
    )



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
            elif choice == "3":
                trip_id = int(input("ID рейса: "))
                name = input("Имя пассажира: ")
                seat = int(input("Номер места: "))

                booking = system.book_ticket(trip_id, name, seat)

                print(
                    f"Билет успешно забронирован! "
                    f"Номер бронирования: {booking.id}"
                )

            elif choice == "4":
                booking_id = int(input("Номер бронирования: "))

                system.cancel_booking(booking_id)

                print("Бронирование отменено.")

            elif choice == "5":
                name = input("Имя пассажира: ")

                system.show_passenger_bookings(name)

            elif choice == "6":
                trip_id = int(input("ID рейса: "))

                seats = system.get_free_seats(trip_id)

                print("Свободные места:", seats)

            elif choice == "7":
                transport_id = int(input("ID транспорта: "))
                kind = input("Тип транспорта: ")
                model = input("Модель: ")
                capacity = int(input("Количество мест: "))
                system.add_transport(
                    Transport(transport_id, kind, model, capacity)
                )

                print("Транспорт добавлен.")

             elif choice == "8":
                trip_id = int(input("ID рейса: "))
                transport_id = int(input("ID транспорта: "))
                departure_city = input("Город отправления: ")
                arrival_city = input("Город прибытия: ")

                departure_time = read_datetime("Отправление: ")
                arrival_time = read_datetime("Прибытие: ")
                price = float(input("Цена билета: "))

                system.add_trip(
                    Trip(
                        trip_id,
                        transport_id,
                        departure_city,
                        arrival_city,
                        departure_time,
                        arrival_time,
                        price
                    )
                )

                print("Рейс добавлен.")

            elif choice == "0":
                print("До свидания!")
                break

            else:
                print("Неизвестная команда.")

        except ValueError as error:
            print("Ошибка:", error)

main()