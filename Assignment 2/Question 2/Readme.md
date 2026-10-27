Employee Management System
Project Overview
The Employee Management System is a Python-based application that uses Object-Oriented Programming (OOP) and file handling to store and manage employee information.
The program stores employee records in a text file (employees.txt) and provides functionality to display employee details, filter employees by salary, find the highest-paid employee, and count employees by designation.
Objectives
Add and store employee records in a text file.
Read and display all employee details.
Find employees whose salary is greater than 50,000.
Identify the employee with the highest salary.
Count the number of employees in each designation.
Reduce code duplication by using a reusable method to read employee records.
Technologies Used
Programming Language: Python
Concepts: Classes, objects, methods, file handling, dictionaries, lists, loops, conditional statements, list comprehension, and exception handling.
Approach and Logic Used
Class Initialization (__init__)
The constructor initializes the file path used to store employee records.
Logic:
Define the path to question2/employees.txt.
Create the parent directory if it does not exist.
Create the file if it does not already exist, without deleting existing records.
B. Adding Employees (add_employee)
This method accepts an employee ID, name, designation, and salary.
Logic:
Open the file in append mode ("a").
Write the employee details as comma-separated values.
Add a newline character so each employee is stored on a separate line.
Example file data:
text
101,Rahul,Python Developer,30000
102,Anjali,Data Scientist,40000
103,Arjun,AI Engineer,60000

Append mode preserves existing records and adds new records at the end of the file.
C. Reading Employee Data (read_employee_data)
This is a reusable method that reads employee records from the file and converts them into a list of dictionaries.
Logic:
Create an empty list named employees.
Open the text file in read mode ("r").
Iterate through the file one line at a time.
Remove whitespace and newline characters using strip().
Split each line using commas with split(",").
Assign the resulting values to employee ID, name, designation, and salary.
Convert the salary from a string to an integer.
Create a dictionary for each employee and append it to the list.
Return the completed list.
Example returned data:
python
[
{
"id": "101",
"name": "Rahul",
"designation": "Python Developer",
"salary": 30000
},
{
"id": "102",
"name": "Anjali",
"designation": "Data Scientist",
"salary": 40000
}
]

Why this method is useful:
Instead of repeating file-reading and parsing logic in every method, the program reads and converts the data in one place. Other methods can reuse the returned list for filtering, comparison, and counting.
D. Displaying All Employees (read_employees)
This method displays the details of every employee.
Logic:
Call read_employee_data() to retrieve the employee records.
Iterate through the returned list.
Print the ID, name, designation, and salary of each employee.
E. Filtering Employees by Salary (employee_salary_gt_50000)
This method displays employees whose salary is strictly greater than 50,000.
Logic:
Retrieve employee records using read_employee_data().
Use list comprehension to filter employees whose salary exceeds 50,000.
Iterate through the filtered list.
Display the name and salary of each qualifying employee.
Example:
python
high_salary_employees = [
emp for emp in employees
if emp["salary"] > 50000
]

This expression creates a new list containing only employees who satisfy the salary condition.
F. Finding the Highest-Paid Employee (employee_highest_salary)
This method identifies the employee or employees who receive the highest salary.
Logic:
Retrieve all employee records.
Check whether the list is empty.
Use max() to find the highest salary.
Use list comprehension to find all employees whose salary equals that maximum.
Display their names and salaries.
Using list comprehension ensures that all employees tied for the highest salary are displayed.
G. Counting Employees by Designation (employee_by_role)
This method counts the number of employees in each designation.
Logic:
Retrieve employee records using read_employee_data().
Create an empty dictionary named role_count.
Iterate through each employee.
Extract the employee's designation.
Increment the count for that designation using dict.get().
Display each designation and its employee count.
Example:
python
role_count[role] = role_count.get(role, 0) + 1

The get() method returns the existing count or 0 if the designation has not been encountered before.
H. Displaying All Results (display_details)
This method acts as the main reporting method.
Logic:
Display all employee details.
Display employees earning more than 50,000.
Display the employee or employees with the highest salary.
Display employee counts grouped by designation.
It calls the other methods using self, keeping the class reusable and avoiding dependence on a global object variable.
Conclusion
This project demonstrates how Python can be used to build a simple employee management application with persistent file storage. The reusable read_employee_data() method separates data reading from business logic, making the program easier to understand, maintain, and extend.
Future improvements could include updating and deleting employee records, validating input, supporting names containing commas through Python's csv module, and migrating from text-file storage to a database.




