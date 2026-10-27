Student Result Management System
Project Overview
The Student Result Management System is a Python-based program that stores student details, calculates academic results, assigns grades, determines pass/fail status, and identifies the student with the highest average score.
The program uses Object-Oriented Programming (OOP) concepts by implementing a Student class.
Objectives
Store student details and subject marks.
Calculate each student's total and average score.
Assign grades based on average marks.
Determine whether a student has passed or failed.
Find the student with the highest average score.
Display students whose average score is above 75.
Approach and Logic Used
Class Initialization (__init__)
The Student class initializes a dictionary to store student records.
students: Stores student details using the student ID as the dictionary key.
Each student record contains the ID, name, and marks in Python, SQL, and AI.
Logic: A dictionary is used to retrieve student records efficiently using their unique IDs.
B. Adding Students (add_student)
This method accepts the student's ID, name, and marks in three subjects.
Logic:
Create a dictionary containing the student's details.
Use the student ID as the key.
Store the student record in the main dictionary.
C. Calculating Grades (calculate_grade)
This method assigns a grade based on the student's average score.
Average Score Grade
80 and above A
60–79.99 B
40–59.99 C
20–39.99 D
Below 20 F
Logic: Conditional statements (if, elif, and else) compare the average score against the grading thresholds.
D. Generating Student Results (student_result)
This method retrieves a student's information using their ID and generates their academic result.
Logic:
Check whether the student ID exists.
Retrieve the student's marks.
Calculate the total score by adding the three subject marks.
Calculate the average score by dividing the total by three.
Call calculate_grade() to determine the grade.
Determine the result:
Average score of 40 or above: PASS
Average score below 40: FAIL
Return the result as formatted text or a dictionary, depending on the implementation.
If the student ID does not exist, the method returns Student not found.
E. Finding the Highest-Average Student (calculate_highest_average)
This method identifies the student with the highest average score.
Logic:
Iterate through all student records.
Calculate each student's total and average score.
Compare the averages to identify the highest one.
Return the name of the student with the highest average.
If there are no students, return No students found.
F. Listing Students Above 75 Average (print_students_with_average_above_75)
This method identifies students whose average score is strictly greater than 75.
Logic:
Iterate through all student records.
Calculate each student's average score.
Check whether the average is greater than 75.
Add qualifying students' names to a list.
Return the list.
Sample Input
python
so = Student()
so.add_student(1, "Alice", 14, 23, 35)
so.add_student(2, "Bob", 78, 82, 88)
Sample Output
text
Student Result:
Student ID: 1
Name: Alice
Total Score: 72
Average Score: 24.0
Grade: D
Result: FAIL
Highest Average Student: Bob
Students with average above 75: ['Bob']
Technologies Used
Programming Language: Python
Concepts: Classes, objects, dictionaries, methods, loops, conditional statements, functions, and string formatting.
Conclusion
This project demonstrates how Python and Object-Oriented Programming can be used to build a simple student result management system. It combines data storage, arithmetic calculations, conditional logic, and iteration to automate common academic result operations.
The program can be extended with features such as updating student details, deleting records, validating marks, sorting students by average, and saving records to a file or database.