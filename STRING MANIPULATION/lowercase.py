def my_tolower(input_string):
    """
    Converts an input string to all lowercase without using built-in string methods.

    Args:
        input_string: The string to convert.

    Returns:
        The lowercase version of the string.
    """
    lowercase_string = ""
    for char in input_string:
        # Get the ASCII value of the character
        ascii_val = ord(char)
        # Check if the character is an uppercase letter (ASCII values 65 to 90)
        if 65 <= ascii_val <= 90:
            # Add 32 to the ASCII value to get the lowercase equivalent
            lowercase_char = chr(ascii_val + 32)
            lowercase_string += lowercase_char
        else:
            # Keep other characters (lowercase letters, numbers, symbols, etc.) unchanged
            lowercase_string += char
    return lowercase_string

# Example usage:
test_string_1 = "HeLLo WoRlD 123!"
test_string_2 = "PYTHON without built-in functions"

print(f"Original: {test_string_1}")
print(f"Lowercase: {my_tolower(test_string_1)}")

print(f"\nOriginal: {test_string_2}")
print(f"Lowercase: {my_tolower(test_string_2)}")
