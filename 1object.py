# object = A "bundle" of related attributes (variables) and methods (functions)

# class = (blueprint) used to design the structure and layout of an object

# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.color = color
#         self.year = year
#         self.for_sale = for_sale

from car1 import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1.model)
print(car1.year)
print(car3.for_sale)

car3.drive()
car2.stop()
car1.describe()
