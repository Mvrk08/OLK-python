"""
Create a class Library that stores a list of books
(each book is a dict with title and author).
Add methods add_book(), remove_book(), and list_books().
"""

class Library :
     def __init__(self):
         self.books = []

     def add_book(self, title: str, author: str):
         book = {"title": title, "author": author}
         self.books.append(book)
         return self.books


     def remove_book(self,update):
         # update=self.books.remove(book)
         # return update
         for book in self.books:
             if book["title"] == title:
                 self.books.remove(book)
                 return True
         return False

     def list_books(self):
         for book in self.books:
             print(book)


library = Library()
library.add_book("Dune", "Frank Herbert")
library.add_book("1984", "George Orwell")

library.list_books()
library.remove_book("Dune")
library.list_books()



