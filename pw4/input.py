
from domains.student import Student
from domains.course import Course


def get_students():
    students = []
    number = int(input("Number of students: "))

    for i in range(number):
        print(f"\nStudent {i + 1}")
        student_id = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of birth: ")

        student = Student(student_id, name, dob)
        students.append(student)

    return students


def get_courses():
    courses = []
    number = int(input("Number of courses: "))

    for i in range(number):
        print(f"\nCourse {i + 1}")
        course_id = input("Course ID: ")
        name = input("Course name: ")
        credits = float(input("Course credits: "))

        course = Course(course_id, name, credits)
        courses.append(course)

    return courses


def get_marks(students, courses):
    for student in students:
        print(f"\nEnter marks for {student.name}")

        for course in courses:
            mark = float(input(f"{course.name} mark: "))
            student.add_mark(course.id, mark)
