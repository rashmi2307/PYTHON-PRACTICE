class fibo:
    def __init__(self, n):
        self.n = n
        print("Fibonacci series up to", n, "terms:")

    def fibo_series(self):
        a, b = 0, 1
        for i in range(self.n):
            print(a, end=" ")
            a, b = b, a+b
n = int(input("Enter the number of terms for Fibonacci series: "))
fibonacci_generator = fibo(n)       
fibonacci_generator.fibo_series()