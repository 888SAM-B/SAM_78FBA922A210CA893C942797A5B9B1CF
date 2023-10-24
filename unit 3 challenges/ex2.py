class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
 
    student_list.sort(key=lambda student: student.cgpa, reverse=True)


students = [
    Student("Bhaargav", "101", 3.9),
    Student("Dharun", "102", 3.5),
    Student("Gautham", "103", 4.0),
    Student("Sam", "104", 3.7),
    Student("Mohit", "105", 3.8)
]


sort_students(students)


for student in students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
