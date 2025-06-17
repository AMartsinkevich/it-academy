def fib():
    fibonacci_first = 0
    fibonacci_second = 1
    while True:
        yield fibonacci_first
        fibonacci_first, fibonacci_second = fibonacci_second, fibonacci_first + fibonacci_second


if __name__ == '__main__':

    reps = int(input('Enter integer of generated numbers: '))
    fibonacci = fib()
    for _ in range(reps+1):
        print(next(fibonacci))
