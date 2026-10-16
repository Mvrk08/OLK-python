"""
Create a class Car with a class variable wheels = 4 shared. Each car has an
instance variable model. Add a class method change_wheel_count(n) and
demonstrate that all existing cars now have the new count.
"""
class Car:
    wheels:int=4
    def __init__(self,name:str,model:str):
        self.name=name
        self.model=model


    def change_wheel_count(self,n):
        cls.wheels=n

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print("Before changing:")
print(car1.wheels)
print(car2.wheels)

Car.change_wheel_count(6)
print("After changing:")
print(car1.wheels)
print(car2.wheels)





