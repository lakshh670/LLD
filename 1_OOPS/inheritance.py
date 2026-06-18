# In this we will see the use of super init function

class Animal:
    def __init__(self, name, age):
        print("Animal init")
        self.name = name
        self.age = age

    def eat(self):
        print("I am eating")
    def sleep(self):
        print("I am sleeping")

class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age) # This is used to invoke the constructor of the parent class.
        self.breed = breed
        print("Dog init")
    def bark(self):
        print("I am barking")

d1=Dog("David",5,"Indie")