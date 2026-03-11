class Book:
    def __init__ (self,price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price
    
    def __lt__(self, other):
        return self.price < other.price

book1 = Book(10)
book2 = Book(20)

total_price = book1 + book2
compare = book1.price < book2.price
print(compare)
print("total_price")

print(int.__add__(2,3))
print(int.__sub__(3,2))