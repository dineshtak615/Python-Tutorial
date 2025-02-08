# library managment software in python
class library:
    def __init__(self,nobooks):
        self.nobooks=nobooks
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def showdetails(self):
        print(f"the library has {self.nobooks} books")  
        for book in self.books:
            print(book) 

l1=library("book in library") 
l1.addbook("harryb potter1")     
l1.addbook("harryb potter2")     
l1.addbook("harryb potter3")     
l1.addbook("harryb potter4")     
l1.showdetails() 
