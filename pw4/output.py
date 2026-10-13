def show_courses(courses):
    print("\nCourses:")
    for course in courses:
        print(f"{course.id} - {course.name} ({course.credits} credits)")


def show_students(students, courses):
    print("\nSTUDENTS SORTED BY GPA:")

    for i, student in enumerate(students, start=1):
        print(f"{i}. {student.name} | ID: {student.id} | GPA: {student.gpa:.2f}")

        for course in courses:
            mark = student.marks.get(course.id, 0)
            print(f"    {course.name}: {mark:.1f}")


def show_ui(students, courses):
    print("\n=== STUDENT MARKS MANAGEMENT ===")
    show_courses(courses)
    show_students(students, courses)
