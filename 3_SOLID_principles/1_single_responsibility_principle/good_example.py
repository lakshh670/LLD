class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self):
        print(f"This is {self.name} and my age is {self.age}")

    def is_adult(self) -> bool:
        return self.age > 18

class UserRepo:
    def __init__(self,db_name,password):
        self.db_name = db_name
        self.password = password
    def save_to_database(self,user:User):
        print(f"{user.name} saved to database")
    def delete_from_database(self,user:User):
        print(f"{user.name} deleted from database")

user_obj = User("John","1234",'')
db=UserRepo("user123",'1234')
user_obj.get_user_info()
db.save_to_database(user_obj)