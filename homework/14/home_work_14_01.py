class Product:

    def __init__(self, name, shop, price):
        self._name = name
        self._shop = shop
        self._price = price

    def __str__(self):
        return f'Product{self._name, self._shop, self._price}'

    def __add__(self, other):
        if isinstance(other, Product):
            return self._price + other._price


class Warehouse:

    def __init__(self, *args):
        self._products = list()
        for item in args:
            self._products.append(item)

    def __str__(self):
        return f'Warehouse with {self._products} products'

    def __getitem__(self, index):
        return self._products[index]
    
    def find_by_name(self, name):
        for item in self._products:
            if item._name == name:
                print(item)

    def sort_by_name(self):
        self._products.sort(key=lambda t: t._name)
        for item in self._products:
            print(item)

    def sort_by_shop(self):
        self._products.sort(key=lambda t: t._shop)
        for item in self._products:
            print(item)

    def sort_by_price(self):
        self._products.sort(key=lambda t: t._price)
        for item in self._products:
            print(item)


if __name__ == '__main__':

    lime = Product('Lime', 'Ki-Ki', 10)
    orange = Product('Orange', 'Loona', 15)

    print(lime)
    print(orange)
    print(lime + orange)

    warehouse = Warehouse(lime, orange)
    print(warehouse[0])
    print(warehouse[1])
    warehouse.find_by_name('Lime')
    warehouse.sort_by_name()
    warehouse.sort_by_shop()
    warehouse.sort_by_price()
