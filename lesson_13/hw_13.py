# # ДЗ 13.1. Група студентів
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
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!


# # ДЗ 13.2. Клас "Цифровий лічильник"
# class Counter:
#
#     def __init__(self, current=1, min_value=0, max_value=10):
#         self.current = current
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def set_current(self, start):
#         try:
#             if self.min_value <= start <= self.max_value:
#                 self.current = start
#             else:
#                 raise ValueError("Start value must be within min and max range.")
#         except ValueError as e:
#             print(e)
#
#     def set_max(self, max_max):
#         try:
#             if max_max >= self.min_value:
#                 self.max_value = max_max
#             else:
#                 raise ValueError("Maximum value must be greater than or equal to minimum value.")
#         except ValueError as e:
#             print(e)
#
#     def set_min(self, min_min):
#         try:
#             if min_min <= self.max_value:
#                 self.min_value = min_min
#             else:
#                 raise ValueError("Minimum value must be less than or equal to maximum value.")
#         except ValueError as e:
#             print(e)
#
#     def step_up(self):
#         try:
#             if self.current < self.max_value:
#                 self.current += 1
#             else:
#                 raise ValueError("Maximum value reached.")
#         except ValueError as e:
#             print(e)
#
#     def step_down(self):
#         try:
#             if self.current > self.min_value:
#                 self.current -= 1
#             else:
#                 raise ValueError("Minimum value reached.")
#         except ValueError as e:
#             print(e)
#
#     def get_current(self):
#         return self.current
#
# # Tests
# counter = Counter()
# counter.set_current(7)
# counter.step_up()
# counter.step_up()
# counter.step_up()
# assert counter.get_current() == 10, 'Test1'
# try:
#     counter.step_up()  # ValueError
# except ValueError as e:
#     print(e)  # Достигнуто максимум
# assert counter.get_current() == 10, 'Test2'
#
# counter.set_min(7)
# counter.step_down()
# counter.step_down()
# counter.step_down()
# assert counter.get_current() == 7, 'Test3'
# try:
#     counter.step_down()  # ValueError
# except ValueError as e:
#     print(e)  # Достигнутий мінімум
# assert counter.get_current() == 7, 'Test4'