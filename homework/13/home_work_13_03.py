class Car:

    def __init__(self, color, type, year):
        self._color = color
        self._type = type
        self._year = year
        self._engine = False

    def engine_on(self):
        self._engine = True

    def engine_off(self):
        self._engine = False

    def status(self):
        print(f'Car of type {self._type}, {self._year} year, {self._color}. Engine is {"on" if self._engine else "off"}')


if __name__ == '__main__':

    car = Car('blue', 'BMW', '2020')
    car.status()
    car.engine_on()
    car.status()
    car.engine_off()
    car.status()
