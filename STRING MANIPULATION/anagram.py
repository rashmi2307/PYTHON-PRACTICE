def are_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if are_anagrams(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")




# without builtin functions

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    count = {}

    # Count characters in first string
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Subtract counts using second string
    for char in str2:
        if char not in count:
            return False
        count[char] -= 1

    # Check if all counts are zero
    for value in count:
        if count[value] != 0:
            return False

    return True


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if are_anagrams(s1, s2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")