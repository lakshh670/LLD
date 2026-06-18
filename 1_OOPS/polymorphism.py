# In this we will see function overriding
class Animal:
    
    def __init__(self, name, age):
        print("Animal init")
        self.name = name
        self.age = age

    def eat(self):
        print("I am eating")
    def sleep(self):
        print("I am sleeping")
    def move(self):
        pass

class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age) # This is used to invoke the constructor of the parent class.
        self.breed = breed
        print("Dog init")
    def bark(self):
        print("I am barking")

    def move(self):
        print("I am moving on 4 legs") # We have overridden the move method