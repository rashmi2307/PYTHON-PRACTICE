number = 1
text = "Rashmi"
values = [1,2,3,4,5]
print(number, type(number))
print(text, type(text))
print(values, type(values))


aa = 10
bb = aa

print(aa is bb) # True, because small integers are cached by Python
print(aa == bb) # True, because their values are equal


value = 10
print("value:", value, "type: ", type(value))

value = "hello"
print("value:", value, "type: ", type(value))

value = [1, 2, 3]
print("value:", value, "type: ", type(value))


numbers = [1, 2, 3, 4, 5]
print("numbers:", numbers, "identity: ", id(numbers))
# Mutable
numbers.append(6)
print("numbers after append:", numbers, "identity: ", id(numbers))

count = 10
print("count:", count, "type: ", type(count))
print("is count an integer?", isinstance(count, int))