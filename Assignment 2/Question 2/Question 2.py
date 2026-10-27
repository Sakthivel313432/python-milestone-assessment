class employee:
    def __init__(self):
        with open("question2/employees.txt", "w") as file:  
            pass
    def add_employee(self, id, name, designation, salary):
        with open("question2/employees.txt", "a") as file:
            file.write(f"{id},{name},{designation},{salary}\n")
    def read_employees(self):
        try:
            with open("question2/employees.txt", "r") as file:
                for line in file:
                    id, name, designation, salary = line.strip().split(",")
                    print(f"ID: {id}, Name: {name}, Designation: {designation}, Salary: {salary}")
        except FileNotFoundError:
            print("No employee file found.")
    def employee_salary_gt_50000(self):
        try:
            with open("question2/employees.txt", "r") as file:
                for line in file:
                    id, name, designation, salary = line.strip().split(",")
                    if int(salary) > 50000:
                        print(f"Name: {name} - Salary: {salary}")
        except FileNotFoundError:
            print("No employee file found.")
    def employee_highest_salary(self):
        highest_salary = 0
        highest_paid_employee = ""
        try:
            with open("question2/employees.txt", "r") as file:
                for line in file:
                    id, name, designation, salary = line.strip().split(",")
                    highest_salary = max(highest_salary, int(salary))
                    if int(salary) == highest_salary:
                        highest_paid_employee = name
            print(f"{highest_paid_employee} - Salary: {highest_salary}")
        except FileNotFoundError:
            print("No employee file found.")

    def employee_by_role(self):
        d={}
        try:
            with open("question2/employees.txt", "r") as file:
                for line in file:
                    id, name, designation, salary = line.strip().split(",")
                    if designation not in d:
                        d[designation] = 1
                    else:
                        d[designation] += 1
        except FileNotFoundError:
            print("No employee file found.")
        for key, value in d.items():
            print(f"{key}: {value}")
    def display_details(self):
        print("=====Employee Details===== \n")
        self.read_employees()
        print("\n=====Employees with Salary greater than 50000===== \n")
        self.employee_salary_gt_50000()
        print("\n=====Employee with Highest Salary===== \n")
        self.employee_highest_salary()
        print("\n=====Employee Count by Role===== \n")
        self.employee_by_role()

emp = employee()
emp.add_employee(101, "Rahul", "Python Developer", 30000)
emp.add_employee(102, "Anjali", "Data Scientist", 40000)
emp.add_employee(103, "Arjun", "AI Engineer", 60000)
emp.add_employee(104, "Neha", "SDET", 35000)
emp.add_employee(105, "Ravi", "Data Scientist", 45000)
emp.add_employee(106, "Simran", "Python Developer", 55000)
emp.display_details()