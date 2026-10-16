"""
Create a class Date with instance variables day, month, year. Add a class
method today() using datetime.date.today() that returns a Date object for
the current date.
"""

from datetime import date

class Date:

    def __init__(self,day:int,month:int,year:int):
        self.day= day
        self.month=month
        self.year=year

    @classmethod
    def current_date(cls) :
      current =date.today()
      return cls(current.day, current.month , current.year)


d = Date.current_date()

print(d.day)
print(d.month)
print(d.year)




