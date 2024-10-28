from Inheritance.Shop.drink import Drink
from Inheritance.Shop.food import Food
from Inheritance.Shop.product_repo import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.product_list)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)