def first_non_repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None


text = input("Enter a string: ")
result = first_non_repeating(text)

if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found.")