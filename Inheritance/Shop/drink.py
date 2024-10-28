from Inheritance.Shop.product import Product


class Drink(Product):

    DEFAULT_QUANTITY: int = 10

    def __init__(self, name):
        super().__init__(name, self.DEFAULT_QUANTITY)

