def fibo_series(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b
n = int(input("Enter the number of terms for Fibonacci series: "))
print("Fibonacci series up to", n, "terms:")
fibonacci_generator = fibo_series(n)
print(fibonacci_generator)