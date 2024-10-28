class Product:
    def __init__(self, name: str, product_quantity: int):
        self.name = name
        self.product_quantity = product_quantity

    def decrease(self, quantity: int):
        if quantity < self.product_quantity:
            self.product_quantity -= quantity


    def increase(self, quantity: int):
        self.product_quantity += quantity


    def __repr__(self):
        return self.name

