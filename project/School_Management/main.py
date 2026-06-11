from abc import ABC, abstractmethod
import json
from pathlib import Path

database = "school_database.json"
data = {"students": [], "teachers": []}

if Path(database).exists():
    with open(database, "r") as file:
        content = file.read()
        if content:
            data = json.loads(content)


def save():
    with open(database, "w") as file:
        json.dump(data, file, indent=4)


class Person(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        return False


class Student(Person):

    def get_roles(self):
        return "Student"

    def register(self):
        name = input("Enter your name:- ")
        age = int(input("Enter your age:- "))
        email = input("Enter your email:- ")
        roll_no = input("Enter your roll number:- ")

        if not Person.validate_email(email):
            print("Invalid email format.")
            return

        for i in data["students"]:
            if i["roll_no"] == roll_no:
                print("Roll number already exists.")
                return

        data["students"].append(
            {
                "name": name,
                "age": age,
                "email": email,
                "roll_no": roll_no,
                "grades": {},
            }
        )

        save()
        print(f"Student {name} registered successfully.")

    def show_details(self):
        # Note: These attributes assume you will instantiate Student with data later
        roll_no = input("Enter your roll number to view details:- ")
        for student in data["students"]:
            if student["roll_no"] == roll_no:
                grades = student['grades']
                avg = sum(grades.values()) / len(grades) if grades else 0
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Email: {student['email']}")
                print(f"Roll No: {student['roll_no']}")
                print(f"Grades: {student['grades']}")
                print(f"Average Grade: {avg:.2f}")
                return  
            
            
            
            
    def add_grades(self):
        roll_no = input("Enter your roll number:- ")
        subject = input("Enter the subject:- ")
        marks = float(input("Enter the marks:- "))

        for student in data["students"]:
            if student["roll_no"] == roll_no:
                student["grades"][subject] = marks
                save()
                print(f"Grade added for {student['name']} in {subject} successfully")
                return

        print("Student with the given roll number not found.")
        


stud = Student()

class Teacher(Person):

    def get_roles(self):
        return "Teacher"

    def register(self):
        name = input("Enter your name:- ")
        age = int(input("Enter your age:- "))
        email = input("Enter your email:- ")
        subject = input("Enter your subject:- ")
        employee_id = input("Enter your employee ID:- ")

        if not Person.validate_email(email):
            print("Invalid email format.")
            return

        for i in data["teachers"]:
            if i["employee_id"] == employee_id:
                print("Employee ID already exists.")
                return

        data["teachers"].append(
            {
                "name": name,
                "age": age,
                "email": email,
                "subject": subject,
                "employee_id": employee_id,
            }
        )

        save()
        print(f"Teacher {name} registered successfully.")

    def show_details(self):
        # Note: These attributes assume you will instantiate Teacher with data later
        employee_id = input("Enter your employee ID to view details:- ")
        for teacher in data["teachers"]:
            if teacher["employee_id"] == employee_id:
                print(f"Name: {teacher['name']}")
                print(f"Age: {teacher['age']}")
                print(f"Email: {teacher['email']}")
                print(f"Subject: {teacher['subject']}")
                print(f"Employee ID: {teacher['employee_id']}")
                return
        
teach = Teacher()

print("press 1 to register a student")
print("press 2 to register a teacher")
print("press 3 to add grades")
print("press 4 to show students details")
print("press 5 to to show teachers details")

choice = input("enter number:- ")

if choice == "1":
    stud.register()
elif choice == "2":
    teach.register()
elif choice == "3":
    stud.add_grades()
elif choice == "4":
    stud.show_details()
elif choice == "5":
    teach.show_details()
else:
    print("Invalid choice.")