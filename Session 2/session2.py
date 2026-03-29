print("Hello, World!")

print(2+3*4)
print((2+3)*4)

first = "Rashmi"
last = "Andhale"
print(first + " " + last)

name = "Rashmi"
print(name[0])  
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[-1])
print(name[-2])
print(name[0:3])
print(name[2:5])
print(name[:3])
print(name[3:])
print(name[::2])


#example 1

def main() -> None:
    whole_number = 15
    decimal_number = 3.14
    piece_of_text = "Hello, World!"
    true_value = True
    print(whole_number, type(whole_number) , end = "\n\n")
    print(decimal_number, type(decimal_number) , sep = "***")
    print(piece_of_text, type(piece_of_text))
    print(true_value, type(true_value) , end = "\n\n")

    number1 = int("25")
    number2 = float("3.14")
    text1 = str(100)
    text2 = str(3.14)
    number3 = int(3.14)

    print(number1, type(number1))
    print(number2, type(number2))
    print(number3, type(number3))


    a = 3
    b = 2
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % b)
    print(a ** b)

    text = "python vibe"

    print(repr(text))
    print(text.strip())
    print(text.replace("python", "java"))
    print(repr(text))


if __name__ == "__main__":    main()

