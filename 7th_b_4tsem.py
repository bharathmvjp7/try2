'''7b.b) Write a python program by creating a class called Employee to store the details of Name,
Employee_ID, Department and Salary and implement a method to update salary of employees
belonging to a given department.
'''
class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def update_salary_by_department(self, new_salary):
        self.salary = new_salary

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print()

def start():
    employees=[]
    dep=[]
    n = int(input("Enter the total number of employees: "))
    
    for i in range(n):
        print("Enter employee details of",i+1,'Employee')
        name = input("Enter Name: ")
        employee_id = input("Enter Employee ID: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        
        dep.append(department)
        employee = Employee(name, employee_id, department, salary)
        employees.append(employee)


    print("All the available Departments are",dep)
    print("to update salary for Departments")
    department_to_update = input("Enter the department to update salary: ")
    new_salary = float(input("Enter the new salary: "))
    
    for employee in employees:
        if employee.department == department_to_update:
            employee.update_salary_by_department(new_salary)

    print("\nUpdated Employee Details:")
    for employee in employees:
        employee.display_details()


start()
