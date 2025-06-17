class BeeElephant:

    def __init__(self, bee, elephant):
        self._bee = bee
        self._elephant = elephant

    def __str__(self):
        return f'BeeElephant{self._bee, self._elephant}'

    def fly(self):
        return self._bee >= self._elephant

    def trumpet(self):
        return 'tu-tu-doo-doo' if self._elephant >= self._bee else 'wzzzz'
    
    def eat(self, meal, value):
        if value > 100:
            value = 100
        if value < 0:
            value = 0
        
        if meal == 'nectar':
            self._bee += value
            self._elephant -= value
        if meal == 'grass':
            self._bee -= value
            self._elephant += value


if __name__ == '__main__':

    beel = BeeElephant(10, 20)
    print(beel)
    print(beel.fly())
    print(beel.trumpet())
    beel.eat('nectar', 20)
    print(beel)
    print(beel.fly())
    print(beel.trumpet())
