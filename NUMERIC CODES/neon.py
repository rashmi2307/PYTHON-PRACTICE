
def is_neon(n):
    return sum(int(digit) for digit in str(n*n)) == n

# Test the function
num = int(input("Enter a number: "))
if is_neon(num):
    print(f"{num} is a Neon number.")
else:
    print(f"{num} is not a Neon number.")