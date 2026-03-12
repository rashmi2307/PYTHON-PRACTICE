def reverse_string(s):
    reversed_str = ""
    
    for char in s:
        reversed_str = char + reversed_str
        
    return reversed_str


# Input
text = input("Enter a string: ")

# Function call
result = reverse_string(text)

print("Reversed string:", result)