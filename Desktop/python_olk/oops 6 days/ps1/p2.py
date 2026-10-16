"""
Create a class Employee with name, salary, and department.
Add a method give_raise(amount) that increases salary.
Create 3 employees and give one of them a raise.
"""


class Employee :
    def __init__(self,name:str,salary:int,department:str):
        self.name=name
        self.salary=salary
        self.department=department

    def give_raise(self,amount:int):
            self.salary+=amount
            # return f"congrats{ self.name} you got {self.salary} in the form of raise"

            return f"congrats {self.name} you got {amount} in the form of raise"



employee1= Employee("alex",10000,"hr")
employee2= Employee("rex",20000,"cfo")
employee3= Employee("james",50000,"cto")

print(employee2.give_raise(40000))




