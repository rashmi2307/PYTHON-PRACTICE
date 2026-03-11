class Payment:
    def __init__(self, price):
        self._final_price = price + price*0.05

def get_final_price(self):
    return self.__final_price

def set_final_price(self, discount):
    return self.__final_price*(discount/100)

book = Payment(10)
# book._final_price = 0
book.set_final_price(10)
print(book._final_price)

hook = Payment(10)