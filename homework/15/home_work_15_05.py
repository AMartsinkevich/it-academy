class Addition:
    def execute(self, a, b):
        return a + b

class Subtraction:
    def execute(self, a, b):
        return a - b

class Multiplication:
    def execute(self, a, b):
        return a * b

class Division:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class Calculator:
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy):
        self._strategy = strategy

    def calculate(self, a, b):
        if not self._strategy:
            raise ValueError("Strategy not set")
        return self._strategy.execute(a, b)

if __name__ == '__main__':

    calc = Calculator()

    calc.set_strategy(Addition())
    print(f'Addition: {calc.calculate(10, 5)}')

    calc.set_strategy(Subtraction())
    print(f'Subtraction: {calc.calculate(10, 5)}')

    calc.set_strategy(Multiplication())
    print(f'Multiplication: {calc.calculate(10, 5)}')

    calc.set_strategy(Division())
    print(f'Division: {calc.calculate(10, 5)}')
