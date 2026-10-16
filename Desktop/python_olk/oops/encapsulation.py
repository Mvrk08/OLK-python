class Bank:
    def __init__(self,name:str,balance:int)->None:
        self.name =name
        self.__balance=balance


    def deposit(self, amount:int):
        if amount<0:
            print("got it")
        else:
           self.__balance+= amount

    def get_balance(self):
        return self.__balance


b1 =Bank("higgs",20000)
print(b1.get_balance())
b1.deposit(1000)
print(b1.get_balance())

