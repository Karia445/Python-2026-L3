
import numpy as np
from input import get_students, get_courses, get_marks
from output import show_ui


def calculate_gpa(student, courses):
    marks = np.array(
        [student.marks.get(course.id, 0) for course in courses],
        dtype=float
    )

    credits = np.array(
        [course.credits for course in courses],
        dtype=float
    )

    total_credits = np.sum(credits)

    if total_credits == 0:
        return 0.0

    return float(np.sum(marks * credits) / total_credits)


def main():
    print("=== Student Marks Management ===")

    students = get_students()
    courses = get_courses()
    get_marks(students, courses)

    for student in students:
        student.gpa = calculate_gpa(student, courses)

    students.sort(key=lambda student: student.gpa, reverse=True)

    show_ui(students, courses)


if __name__ == "__main__":
    main()
