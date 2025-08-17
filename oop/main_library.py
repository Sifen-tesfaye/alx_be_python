# main_library.py
from library_system import Book, EBook, PrintBook, Library
   
#create library
library = Library()
    
# Add books 

library.add_book(Book("Pride and Prejudice", "Jane Austen"))
library.add_book(EBook("Snow Crash", "Neal Stephenson", 500))
library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))
 # Display books 
library.list_books()


