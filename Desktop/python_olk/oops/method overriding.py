class Animal :
    def  speak(self):
        print("animal is speaking")

    def display(self):
        print("this is display fn")


class Dog(Animal):
    def speak(self):
        super().speak()
        super().display()

        print("dog is speaking")



d=Dog()
d.speak()
