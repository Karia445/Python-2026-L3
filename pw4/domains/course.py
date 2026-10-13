
class Course:
    def __init__(self, course_id, course_name, credits):
        self.id = course_id
        self.name = course_name
        self.credits = credits

    def __str__(self):
        return f"ID: {self.id}, Course: {self.name}, Credits: {self.credits}"
