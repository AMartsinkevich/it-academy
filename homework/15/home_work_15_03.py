class Pizza:
    def __init__(self, size=None, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        toppings = []
        if self.cheese: toppings.append("cheese")
        if self.pepperoni: toppings.append("pepperoni")
        if self.mushrooms: toppings.append("mushrooms")
        if self.onions: toppings.append("onions")
        if self.bacon: toppings.append("bacon")
        toppings_str = ", ".join(toppings) if toppings else "no toppings"
        return f"Pizza(size={self.size}, toppings=[{toppings_str}])"

class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(
            size=self.size,
            cheese=self.cheese,
            pepperoni=self.pepperoni,
            mushrooms=self.mushrooms,
            onions=self.onions,
            bacon=self.bacon
        )


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, size, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.builder.set_size(size)
        if cheese:
            self.builder.add_cheese()
        if pepperoni:
            self.builder.add_pepperoni()
        if mushrooms:
            self.builder.add_mushrooms()
        if onions:
            self.builder.add_onions()
        if bacon:
            self.builder.add_bacon()
        return self.builder.build()


if __name__ == '__main__':

    builder = PizzaBuilder()
    director = PizzaDirector(builder)
    pizza = director.make_pizza(size="Large", cheese=True, pepperoni=True, bacon=True)
    print(pizza)
