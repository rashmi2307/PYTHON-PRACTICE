# Inheritance = Allows a class to inherit attributes and methods from another class 
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__ (self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Mouse(Animal):
    def speak(self):
        print("squeak")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(cat.is_alive)
dog.eat()
cat.sleep()
mouse.speak()