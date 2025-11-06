# object_oriented_db.py
# Simulation of an Object Oriented Database for a College System

import pickle  # Used to store (serialize) objects in a binary file

# Define classes (like real-world entities)
class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}")


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

# Create sample objects
s1 = Student(101, "Amit Sharma", "Computer Science")
s2 = Student(102, "Neha Patil", "Information Technology")
s3 = Student(103, "Ravi Kumar", "Data Science")



# Store (serialize) objects in a binary file
with open("students_database.pkl", "wb") as file:
    pickle.dump([s1, s2, s3], file)

print("Objects have been stored successfully in 'students_database.pkl'")

# Retrieve (deserialize) objects from file
with open("students_database.pkl", "rb") as file:
    students = pickle.load(file)

print("\nStored Students:")
for s in students:
    s.display()
