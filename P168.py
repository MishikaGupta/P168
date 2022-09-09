# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 15:54:20 2022

@author: Beautiful Mishika
"""

class Book:
    def __init__(self, name,author_name, publish_date, cost):
        self.book_name = name
        self.book_author = author_name
        self.book_published = publish_date
        self.book_cost = cost
    
    def add_book(self):
        print("Name Of The Book: " + self.book_name)
        print("Author: " + self.book_author)
        print("Published On: " + str(self.book_published))
        print("Cost " + str(self.book_cost))
        print("BOOK ADDED")
        
    
book1 = Book("The Diary Of A Young Girl", "Anne Frank", "14th June 1942" ,349 )
book1.add_book()

book2 = Book("Wonder", "R.J. Palacio", "14th February 2012",  399)
book2.add_book()