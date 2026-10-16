"""
Create a class Movie with attributes title, director, year, rating.
Add a method is_classic() that returns True if the movie is more than 25 years old.
"""

class Movie:
    def __init__(self,title:str,director:str,year:int):
        self.title=title
        self.director= director
        self.year = year



    def  is_classic(self) ->bool:
        if self.year >= 2025 :
            return True
        else :
           return False



##### book1 = Book("Atomic Habits", "James Clear", 320)


movie1 =Movie("toy story2", "john lasster", "1999")
movie2 =Movie("dhurandhar", "aditya dhar", "2026")

movie1.is_classic()
movie2.is_classic()

