""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Vehicle = brand:{self.brand},model :{self.model},year : {self.year}"

class car(Vehicle):
    def __init__(self,brand, model, year,number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Vehicle = brand:{self.brand},model :{self.model},year : {self.year},number_of_doors :{self.number_of_doors}"

vehicle = Vehicle("Honda", "CBR650R", 2023)
print(vehicle.get_info())

Car = car("Honda", "Civic", 2025, 4)
print(Car.get_info())