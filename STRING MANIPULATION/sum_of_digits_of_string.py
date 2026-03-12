def sum_of_digits(s):
    total = 0
    
    for char in s:
        digit = int(char)   # convert character to integer
        total += digit      # add to total
        
    return total


num_string = input("Enter a string of digits: ")
result = sum_of_digits(num_string)

print("Sum of digits:", result)