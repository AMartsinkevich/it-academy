class Math:

    def addition(self, a: int, b: int) -> int:
        return a + b

    def subtraction(self, a: int, b: int) -> int:
        return a - b

    def multiplication(self, a: int, b: int) -> int:
        return a * b

    def division(self, a: int, b: int) -> float:
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError


if __name__ == '__main__':

    math = Math()
    print(math.addition(1, 2))
    print(math.subtraction(1, 2))
    print(math.multiplication(1, 2))
    print(math.division(1, 2))
