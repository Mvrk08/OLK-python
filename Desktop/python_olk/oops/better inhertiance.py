class Animal:
    def __init__(self, name:str,age:int)->None:
        self.name=name
        self.age=age

    def speak(self):
        print(self.name)

    def sleep(self):
        print(self.name)


class Dog(Animal):
    def bark(self):
        print(self.name)


d1 =Dog("abc",21)
d1.sleep ()
d1.speak()
d1.bark()
print(d1.age)

