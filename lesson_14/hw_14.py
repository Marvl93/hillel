#ДЗ 14.1. Виняток користувача
class GroupLimitError(Exception):
    """Custom exception raised when trying to add more than 10 students to a group."""
    def __init__(self, message="Group cannot have more than 10 students."):
        self.message = message
        super().__init__(self.message)

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        if isinstance(student, Student):
            self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group Number: {self.number}\nStudents:\n{all_students}"

# Testing
try:
    gr = Group('PD1')

    for i in range(1, 12):  # Attempt to add 11 students
        student = Student('Male', 20 + i, f'Name{i}', f'LastName{i}', f'RB{i:03}')
        gr.add_student(student)
        print(f"Added: {student}")

except GroupLimitError as e:
    print(f"Exception: {e}")

print("\nFinal group:\n")
print(gr)
