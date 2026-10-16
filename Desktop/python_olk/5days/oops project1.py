"""
bank  management  system
"""

class BankAccount:

    def __init__(self, name: str, acc_no: int) -> None:
        self.name = name
        self.acc_no = acc_no
        self.balance = 0
        self.transaction = []


    def deposit(self,amount:int)-> int:
        # amount=0
        if self.balance>= 500 or self.balance>=0 :
            return self.balance
        self.balance += amount
        self.transaction.append(f"Deposited: {amount}")  ##### point to be noted
        return self.balance


    def withdraw(self,balance:int)-> int:


    def check_balance(self):
        pass

    def view_history(self):
        pass


