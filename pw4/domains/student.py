
class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.2f}"

