# Single Responsibility Principle (SRP)
# Definition: A class should have only one reason to change, meaning
# it should do only one job or have only one responsibility.

# Simple terms: "Don't make one class do everything.
# Each class should focus on one task only."

# Example: A User class should only handle user-related data,
# while database operations should be handled by
# a separate UserRepository class.

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self):
        print(f"This is {self.name} and my age is {self.age}")

    def is_adult(self) -> bool:
        return self.age > 18

    def save_to_database(self):
        print(f"{self.name} is getting saved to Database")

    def delete_user_from_database(self):
        print(f"{self.name} is getting deleted from Database") # Both User related and database related works are done in same class.
