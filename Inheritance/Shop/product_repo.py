from typing import List

from Inheritance.Shop.product import Product


class ProductRepository:
    def __init__(self):
        self.product_list: List = []


    def add(self, product: Product):
        if not product in self.product_list:
            self.product_list.append(product)

    def find(self, product):

        for p in self.product_list:
            if p.name == product:
                return p

    def remove(self, product):
        self.product_list.remove(product)


    def __repr__(self):
        result =""
        for item in self.product_list:
          result += f"{item.name}: {item.product_quantity}\n"
        return result