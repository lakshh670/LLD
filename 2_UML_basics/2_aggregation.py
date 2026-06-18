# Weak 'has-a' relationship if the contained objects may exist when the container is destroyed.

class Student:
    def __init__(self,name:str,roll_no:int):
        self.__name=name
        self.__roll_no=roll_no
    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no

class Department:
    def __init__(self,department_name:str):
        self.__department_name=department_name
        self.students=[]
    def add_student(self,student:Student):
        self.students.append(student)

    def show_students(self) -> None:
        print(f"\nStudents in {self.__dept_name} Department:")
        for student in self.__students:
            print(f"  - {student.get_name()} (Roll No: {student.get_roll_no()})")

# Creating Student objects (they exist independently)
student1: Student = Student("Rahul", 101)
student2: Student = Student("Priya", 102)
student3: Student = Student("Amit", 103)

# Creating Department object
cs_dept: Department = Department("Computer Science")

# Adding students to department (Aggregation happening here!)
cs_dept.add_student(student1)
cs_dept.add_student(student2)
cs_dept.add_student(student3)

# Display students
cs_dept.show_students()

# IMPORTANT: Even if we delete the department, students still exist!
del cs_dept  # Department deleted

# Students are still alive and can be used
print(f"\nStudent still exists: {student1.get_name()}")
# Output: Student still exists: Rahul
