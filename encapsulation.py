class Payment:
    def __init__(self, price):
        self._final_price = price + price*0.05

    def get_final_price(self):
        return self._final_price

    def set_final_price(self, discount):
        self._final_price = self._final_price - self._final_price*(discount/100)

    def _calculate_discount(self, discount):
        return self._final_price * (discount/100)

book = Payment(10)
# book._final_price = 0
book._calculate_discount(50)
book.set_final_price(10)
print(book.get_final_price())

hook = Payment(10)