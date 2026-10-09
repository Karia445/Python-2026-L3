student_numbers = int(input('Number of students:'))

students = []

for i in range(student_numbers):
    student_name = input('name: ')
    student_id = input('id: ')
    student_DoB = input('DoB: ')

    student = {
        'id': student_id,
        'name': student_name,
        'DoB': student_DoB
    }

    students.append(student)
course_numbers = int(input('enter the number of course:'))
courses =[]
for i in range (course_numbers):
    course_name = input('course name: ')
    course_id = input('course id: ')
courses.append({
    'course_id': course_id,
    'course_name': course_name
})
selected_course = input('Choose course id: ')
course_mark = input('mark: ')
#listing
print("students:")

for student in students:
    print(student)
print("courses:")
for courses in courses :
  print(courses)
print("course:", selected_course)
print("student:", student['name'])
print("mark:", course_mark)