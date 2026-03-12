def even_odd(num):
    if num % 2 == 0:
        return "{num} is an even number"
    else:
        return "{num} is an odd number"
number = int(input("Enter a number to check if it is even or odd: "))
result = even_odd(number)
print(result.format(num=number))