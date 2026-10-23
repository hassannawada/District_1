from abc import ABC, abstractmethod

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def __str__(self):                       
        if self.available:
            return self.title + " (available)"
        return self.title + " (borrowed)"

class Member(ABC):                          
    limit = 2                                

    def __init__(self, name):
        self.name = name
        self.books = []                     

    @abstractmethod
    def fine(self, late_days):               
        pass

    def borrow(self, book):
        if not book.available:
            print(book.title, "is already borrowed")
        elif len(self.books) >= self.limit:
            print(self.name, "reached the limit of", self.limit, "books")
        else:
            self.books.append(book)
            book.available = False
            print(self.name, "borrowed", book.title)

    def give_back(self, book, late_days):
        self.books.remove(book)
        book.available = True
        print(self.name, "returned", book.title, "| fine: Rs", self.fine(late_days))

    def __len__(self):                       # len(member) = number of books
        return len(self.books)

    def __str__(self):
        return self.name + " has " + str(len(self)) + " book(s)"

class StandardMember(Member):                
    limit = 2
    def fine(self, late_days):
        return late_days * 10

class PremiumMember(StandardMember):        
    limit = 5
    def fine(self, late_days):              
        return late_days * 5

class VIPMember(PremiumMember):           
    limit = 10
    def fine(self, late_days):               
        return 0

# ---- test ----
b1 = Book("Python Basics")
b2 = Book("Data Science")
b3 = Book("Algorithms")

ali = StandardMember("Ali")
sara = PremiumMember("Sara")
usman = VIPMember("Usman")

ali.borrow(b1)
sara.borrow(b1)        
ali.borrow(b2)
ali.borrow(b3)          

ali.give_back(b1, 10)    
sara.borrow(b1)
sara.give_back(b1, 10)   
usman.borrow(b3)
usman.give_back(b3, 10) 

print(ali)
print(b1)
