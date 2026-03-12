def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring case and spaces.

    A palindrome is a word, phrase, or sequence that reads the same 
    backward as forward. This function handles typical variations by 
    stripping non-alphanumeric characters and converting to lowercase.
    """
    # Create a new string with only alphanumeric characters, all in lowercase
    # This handles spaces, punctuation, and case sensitivity (e.g., 'Racecar' == 'racecar')
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse using slicing
    # 'cleaned_string[::-1]' reverses the string
    return cleaned_string == cleaned_string[::-1]

# --- Examples ---

# True: 'madam' is a palindrome
print(f"'madam': {is_palindrome('madam')}")

# True: 'A man, a plan, a canal: Panama' is a palindrome (ignoring non-alphanumeric)
print(f"'A man, a plan, a canal: Panama': {is_palindrome('A man, a plan, a canal: Panama')}")

# False: 'hello' is not a palindrome
print(f"'hello': {is_palindrome('hello')}")

# True: 'Racecar' is a palindrome (case insensitive)
print(f"'Racecar': {is_palindrome('Racecar')}")
