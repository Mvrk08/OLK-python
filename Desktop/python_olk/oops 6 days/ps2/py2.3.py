"""
Create a Validator class with static methods: is_email(s), is_phone(s),
is_strong_password(s). Each returns True or False.
"""



class Validator :
    def __init__(self,email:str, phone :int,strong_password:str ) :
        self.email=email
        self.phone=phone
        self.strong_password=strong_password



        @staticmethod
        def  is_email()


