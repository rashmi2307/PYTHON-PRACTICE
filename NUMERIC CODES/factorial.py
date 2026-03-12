def factorial(num):
    if num <0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
number = int(input("Enter a number to calculate its factorial: "))
result = factorial(number)  
print(f"The factorial of {number} is: {result}")
