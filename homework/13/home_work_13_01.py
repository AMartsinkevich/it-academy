class Soda:

    def __init__(self, taste=None):
        self._taste = taste

    def __str__(self):
        return f'Soda with {self._taste} taste' if self._taste else 'Ordinary soda'


if __name__ == '__main__':

    soda_no_taste = Soda()
    soda_orange_taste = Soda('orange')

    print(soda_no_taste)
    print(soda_orange_taste)
