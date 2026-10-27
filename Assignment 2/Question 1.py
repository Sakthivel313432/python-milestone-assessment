class Student:
    def __init__(self):
        self.Students = {}
        self.Student_average = []

    def add_student(self, id, name, python, sql, ai):
        student = {
            "id": id,
            "name": name,
            "python": python,
            "sql": sql,
            "ai": ai
        }
        self.Students[student["id"]] = student

    def calculate_grade(self, average_score):
        if average_score >= 80:
            return "A"
        elif average_score >= 60:
            return "B"
        elif average_score >= 40:
            return "C"
        elif average_score >= 20:
            return "D"
        else:
            return "F"

    def student_result(self, id):
        if id in self.Students:
            student = self.Students[id]
            total_score = (
                student["python"] +
                student["sql"] +
                student["ai"]
            )
            average_score = total_score / 3

            return (
                f"Student ID: {student['id']}\n"
                f"Name: {student['name']}\n"
                f"Total Score: {total_score}\n"
                f"Average Score: {average_score:.2f}\n"
                f"Grade: {self.calculate_grade(average_score)}\n"
                f"Result: {'PASS' if average_score >= 40 else 'FAIL'}\n"
            )
        else:
            return "Student not found"

    def calculate_highest_average(self):
        highest_average = 0
        top_student = None

        for student in self.Students.values():
            total_score = (
                student["python"] +
                student["sql"] +
                student["ai"]
            )
            average_score = total_score / 3

            if average_score >= 75:
                self.Student_average.append(student["name"])

            if average_score > highest_average:
                highest_average = average_score
                top_student = student

        if top_student:
            return top_student["name"]
        else:
            return "No students found"

    def print_students_with_average_above_75(self):
        return self.Student_average

    def get_all_students(self):
        for student in self.Students.values():
            print(
                f"ID: {student['id']}, "
                f"Name: {student['name']}, "
                f"Python: {student['python']}, "
                f"SQL: {student['sql']}, "
                f"AI: {student['ai']}"
            )


# Object creation
so = Student()

# Add students
so.add_student(1, "Alice", 14, 23, 35)
so.add_student(2, "Bob", 78, 82, 88)
so.add_student(3, "Charlie", 45, 55, 65)
so.add_student(4, "David", 90, 92, 95)

# Display single student result
print("===== Student Result =====")
print(so.student_result(1))
print(so.student_result(2))

# Display all students results
print("===== All Student Results =====")
for s in so.Students.keys():
    print(so.student_result(s))

# Highest average student
print("Highest Scoring Student:", so.calculate_highest_average())
