class Parent:
    def swap_second_half(self, list_a, list_b):
        n = len(list_a) // 2
        
        # Swap second halves
        temp = list_a[n:]
        list_a[n:] = list_b[n:]
        list_b[n:] = temp
        
        return list_a, list_b


class Child(Parent):
    pass


# Given lists
list_a = ['a', 'b', 'c', 'd']
list_b = ['e', 'f', 'g', 'h']

# Create object of child class
obj = Child()

# Call inherited function
new_a, new_b = obj.swap_second_half(list_a, list_b)

print("list_a becomes", new_a)
print("list_b becomes", new_b)