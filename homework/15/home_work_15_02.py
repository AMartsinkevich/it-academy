def generator():
    cur = 1
    while True:
        yield cur
        if cur < 3:
            cur += 1
        else:
            cur = 1


if __name__ == '__main__':

    reps = int(input('Enter integer of generated numbers: '))
    sequence = generator()
    for _ in range(reps+1):
        print(next(sequence))
