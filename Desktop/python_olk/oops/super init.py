class Vehicle:
    def __init__(self,brand:str)->None:
        print("this is vehicle constructor")
        self.brand=brand


class Car(Vehicle):
    def __init__(self, fuel: str, brand:str) -> None:
        super().__init__(brand)
        print("this is car constructor")
        self.fuel=fuel

    def display(self):
        print(f"you got {self.brand} car of this {self.fuel} variant")



car=Car("petrol","range rover")
car.display()

