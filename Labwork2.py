import math
import numpy as np
import curses


def get_students():
    students = []
    student_numbers = int(input("Number of students: "))

    for i in range(student_numbers):
        print(f"\nStudent {i + 1}")
        student_name = input("Name: ")
        student_id = input("ID: ")
        student_DoB = input("DoB: ")

        students.append({
            "id": student_id,
            "name": student_name,
            "DoB": student_DoB,
            "marks": {},
            "GPA": 0.0
        })

    return students


def get_courses():
    courses = []
    course_numbers = int(input("\nEnter the number of courses: "))

    for i in range(course_numbers):
        print(f"\nCourse {i + 1}")
        course_name = input("Course name: ")
        course_id = input("Course ID: ")
        credits = float(input("Course credits: "))

        courses.append({
            "course_id": course_id,
            "course_name": course_name,
            "credits": credits
        })

    return courses


def get_marks(students, courses):
    print("\nEnter marks from 0 to 10.")

    for student in students:
        print(f"\nMarks for {student['name']} ({student['id']})")
        for course in courses:
            while True:
                try:
                    mark = float(input(
                        f"{course['course_name']} ({course['course_id']}): "
                    ))
                    if 0 <= mark <= 10:
                        break
                    print("Please enter a mark between 0 and 10.")
                except ValueError:
                    print("Please enter a valid number.")

            # Round down to one decimal place.
            mark = math.floor(mark * 10) / 10
            student["marks"][course["course_id"]] = mark


def calculate_gpa(student, courses):
    if not courses:
        return 0.0

    marks = np.array([
        student["marks"][course["course_id"]] for course in courses
    ], dtype=float)
    credits = np.array([course["credits"] for course in courses], dtype=float)

    total_credits = np.sum(credits)
    if total_credits == 0:
        return 0.0

    return float(np.sum(marks * credits) / total_credits)


def show_ui(students, courses):
    def draw_screen(screen):
        curses.curs_set(0)
        screen.clear()
        screen.addstr(0, 2, "STUDENT AND COURSE MARKS", curses.A_BOLD)
        screen.addstr(2, 2, "Courses:", curses.A_UNDERLINE)

        row = 3
        for course in courses:
            line = (f"{course['course_id']} - {course['course_name']} "
                    f"({course['credits']} credits)")
            if row < curses.LINES - 2:
                screen.addstr(row, 2, line[:curses.COLS - 4])
                row += 1

        row += 1
        if row < curses.LINES - 1:
            screen.addstr(row, 2, "Students sorted by GPA:", curses.A_UNDERLINE)
            row += 1

        for index, student in enumerate(students, start=1):
            marks_text = ", ".join(
                f"{course['course_id']}: {student['marks'][course['course_id']]:.1f}"
                for course in courses
            )
            line = (f"{index}. {student['name']} | ID: {student['id']} | "
                    f"GPA: {student['GPA']:.2f} | {marks_text}")
            if row < curses.LINES - 1:
                screen.addstr(row, 2, line[:curses.COLS - 4])
                row += 1

        if curses.LINES > 1:
            screen.addstr(curses.LINES - 1, 2, "Press any key to exit")
        screen.refresh()
        screen.getch()

    try:
        curses.wrapper(draw_screen)
    except curses.error:
        # Fallback for terminals that do not support curses properly.
        print("\nSTUDENT AND COURSE MARKS")
        print("Courses:")
        for course in courses:
            print(f"{course['course_id']} - {course['course_name']} ({course['credits']} credits)")
        print("\nStudents sorted by GPA:")
        for index, student in enumerate(students, start=1):
            print(f"{index}. {student['name']} | ID: {student['id']} | GPA: {student['GPA']:.2f}")


def main():
    print("=== Student Marks Management ===")
    students = get_students()
    courses = get_courses()
    get_marks(students, courses)

    for student in students:
        student["GPA"] = calculate_gpa(student, courses)

    students.sort(key=lambda student: student["GPA"], reverse=True)
    show_ui(students, courses)


if __name__ == "__main__":
    main()
