from Inheritance.Need_For_Speed.family_car import FamilyCar
from Inheritance.Need_For_Speed.sport_car import SportCar
from Inheritance.Need_For_Speed.vehicle import Vehicle

vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
race_car = SportCar(150, 150)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)