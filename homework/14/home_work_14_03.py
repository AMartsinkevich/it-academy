class Bus:

    def __init__(self, capacity, speedlimit, passengers):
        self._speed = 0
        self._capacity = capacity
        self._speedlimit = speedlimit
        self._passengers = list()
        self._passengers.extend(passengers)
        self._is_free = True
        self._seats = {}
        if len(self._passengers) > self._capacity:
            self._is_free = False

    def seat_in(self, passengers):
        self._passengers.extend(passengers)
        if len(self._passengers) > self._capacity:
            self._is_free = False
    
    def seat_out(self, passengers):
        for passenger in passengers:
            self._passengers.remove(passenger)
        if len(self._passengers) < self._capacity:
            self._is_free = True

    def speed_up(self, value):
        self._speed += value

    def speed_down(self, value):
        self._speed -= value
    
    def __contains__(self, passenger):
        return passenger in self._passengers
    
    def __iadd__(self, passenger):
        self._passengers.append(passenger)
        if len(self._passengers) > self._capacity:
            self._is_free = False
        return self

    def __isub__(self, passenger):
        self._passengers.remove(passenger)
        if len(self._passengers) < self._capacity:
            self._is_free = True
        return self


if __name__ == '__main__':

    bus = Bus(20, 40, ['Me', 'You'])
    print(bus._speed)
    bus.speed_up(10)
    print(bus._speed)
    bus.speed_down(10)
    print(bus._speed)
    print('You' in bus)
    bus += 'Kitty'
    print('Kitty' in bus)
    bus -= 'Kitty'
    print('Kitty' in bus)
