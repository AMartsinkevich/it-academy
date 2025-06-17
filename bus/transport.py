# from abc import ABC, abstractmethod, abstractproperty
# import uuid
#
# class Transport(ABC):
#
#     @abstractmethod
#     def book_seat(self, seat_number):
#         pass
#
#     @abstractmethod
#     def get_available_seats(self):
#         pass
#
#     @abstractmethod
#     def get_info(self):
#         pass
#
#
# class Bus(Transport):
#
#     def __init__(self, capacity, way):
#         self.id = uuid.uuid4()
#         self.capacity = capacity
#         self.booked_seats = 0
#         self.way = way
#
#     def get_info(self):
#         return f'Bus №{self.way}, {self.capacity} мест'
#
#     def book_seat(self, seat_number):
#         if self.booked_seats + seat_number >= self.capacity:
#             print('No free space')
#         else:
#             self.booked_seats += seat_number
#
#     def get_available_seats(self):
#         return self.capacity - self.booked_seats
#
#
# class Train(Transport):
#
#     def __init__(self, capacity, number_of_wagons):
#         self.id = uuid.uuid4()
#         self.capacity = capacity
#         self.booked_seats = 0
#         self.number_of_wagons = number_of_wagons
#
#     def get_info(self):
#         return f'Train №456, {self.capacity} мест, вагоны: {self.number_of_wagons}'
#
#     def book_seat(self, seat_number):
#         if self.booked_seats + seat_number >= self.capacity:
#             print('No free space')
#         else:
#             self.booked_seats += seat_number
#
#     def get_available_seats(self):
#         return self.capacity - self.booked_seats
#
#
# class Plane(Transport):
#
#     def __init__(self, capacity, model):
#         self.id = uuid.uuid4()
#         self.capacity = capacity
#         self.booked_seats = 0
#         self.model = model
#
#     def get_info(self):
#         return f'Plane №789, {self.capacity} мест, модель: {self.model}'
#
#     def book_seat(self, seat_number):
#         if self.booked_seats + seat_number >= self.capacity:
#             print('No free space')
#         else:
#             self.booked_seats += seat_number
#
#     def get_available_seats(self):
#         return self.capacity - self.booked_seats
#
#
# class Passenger:
#     def __init__(self, name, passport):
#         self.name = name
#         self.passport = passport
#
#     def __str__(self):
#         return f'Passenger {self.name}, паспорт: {self.passport}'
#
# if __name__ == '__main__':
#     bus = Bus(40, 123)
#     train = Train(100, 10)
#     plane = Plane(120, 'Boeing A777')
#
#     print(bus.get_info())
#     print(train.get_info())
#     print(plane.get_info())
#
#     print(bus.id)
#
#
#





from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, id: int, capacity: int):
        self.id = id
        self.capacity = capacity
        self.booked_seats = []

    def book_seat(self, seat_number: int) -> bool:
        if 1 <= seat_number <= self.capacity and seat_number not in self.booked_seats:
            self.booked_seats.append(seat_number)
            return True
        return False

    def get_available_seats(self):
        return [seat for seat in range(1, self.capacity + 1) if seat not in self.booked_seats]

    @abstractmethod
    def get_info(self) -> str:
        pass

    def __str__(self):
        return f"{self.__class__.__name__} №{self.id}, свободных мест: {len(self.get_available_seats())}"


class Bus(Transport):
    def __init__(self, id: int, capacity: int, route: str):
        super().__init__(id, capacity)
        self.route = route

    def get_info(self) -> str:
        return f"Bus №{self.id}, {self.capacity} мест, маршрут: {self.route}"


class Train(Transport):
    def __init__(self, id: int, capacity: int, wagons: int):
        super().__init__(id, capacity)
        self.wagons = wagons

    def get_info(self) -> str:
        return f"Train №{self.id}, {self.capacity} мест, вагоны: {self.wagons}"


class Plane(Transport):
    def __init__(self, id: int, capacity: int, model: str):
        super().__init__(id, capacity)
        self.model = model

    def get_info(self) -> str:
        return f"Plane №{self.id}, {self.capacity} мест, модель: {self.model}"


class Passenger:
    def __init__(self, name: str, passport_number: str):
        self.name = name
        self.passport_number = passport_number

    def __str__(self):
        return f"Passenger {self.name}, паспорт: {self.passport_number}"


class Booking:
    def __init__(self, passenger: Passenger, transport: Transport, seat_number: int):
        self.passenger = passenger
        self.transport = transport
        self.seat_number = seat_number

    def confirm(self) -> str:
        if self.transport.book_seat(self.seat_number):
            return (f"Booked: {self.passenger.name}, "
                    f"место {self.seat_number} в {self.transport.__class__.__name__} №{self.transport.id}")
        else:
            return f"Error: Seat {self.seat_number} is absent or busy."

    def __repr__(self):
        return (f"<Booking: {self.passenger.name}, место {self.seat_number} в "
                f"{self.transport.__class__.__name__} №{self.transport.id}>")


class BookingSystem:
    def __init__(self):
        self.transports = {}
        self.bookings = []

    def add_transport(self, transport: Transport):
        self.transports[transport.id] = transport

    def make_booking(self, passenger: Passenger, transport_id: int, seat_number: int) -> str:
        transport = self.transports.get(transport_id)
        if not transport:
            return f"Транспорт с id {transport_id} не найден."
        booking = Booking(passenger, transport, seat_number)
        confirmation = booking.confirm()
        if confirmation.startswith("Бронь подтверждена"):
            self.bookings.append(booking)
        return confirmation

    def list_bookings(self):
        if not self.bookings:
            print("Nothing to show.")
            return
        for booking in self.bookings:
            print(booking)


if __name__ == "__main__":
    system = BookingSystem()

    bus = Bus(123, 40, "Маршрут 10")
    train = Train(456, 100, 10)
    plane = Plane(789, 150, "Boeing 737")

    system.add_transport(bus)
    system.add_transport(train)
    system.add_transport(plane)

    passenger1 = Passenger("Иван Иванов", "AA123456")
    passenger2 = Passenger("Мария Петрова", "BB654321")

    print(system.make_booking(passenger1, 123, 12))
    print(system.make_booking(passenger2, 456, 5))
    print(system.make_booking(passenger1, 789, 1))
    print(system.make_booking(passenger2, 123, 12))

    print("\nInfo:")
    print(bus.get_info())
    print(train.get_info())
    print(plane.get_info())

    print("\nBooks:")
    system.list_bookings()

    print("\nStatistics:")
    print(bus)
    print(train)
    print(plane)
