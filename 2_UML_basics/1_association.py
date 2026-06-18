class Student:
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

class Teacher:
    def __init__(self,name):
        self.__name=name

    def teach(self,student:Student):
        print(f"{self.__name} teaches {student.get_name()}")


t1=Teacher("Sharma Sir")
s1=Student("Rahul")
t1.teach(s1)