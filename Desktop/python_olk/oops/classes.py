class Student:

     def __init__(self,roll_no:int,name:str,gender:str,age:int)->None:

        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.gender = gender


    # methods
    def display_details(self)-> None:
        print(f"Roll no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")

        print("---------------")


# object / instance
student1 = Student(22,"maahir","male",1)
# # student1.set_details(22,"maahir","male",1)
# student1.display_details()

