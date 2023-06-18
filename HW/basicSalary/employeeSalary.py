'''
Define a class for an employee.
Add a method to calculate the salary of the employee in that class based on the number of hrs worked.

In the main program, you are starting a new companyy. Hiring a few employees. Each one has different per hr
salary.

Get input from the owner of the company on how many hrs each employee worked.
Display the details of the employee who has the highest salary
'''

#define the employee class.
class Employee:
    def __init__(self, name, salaryPerHour):
        self.name = name
        self.salaryPerHour = salaryPerHour

    def calculate_salary(self, hoursWorked):
        return self.salaryPerHour * hoursWorked

num_employees = int(input("Enter the number of employees: "))
employees = []

for i in range(num_employees):
    name = input("Enter employee name: ")
    salaryPerHour = float(input("Enter per hour salary for {}: ".format(name)))
    employee = Employee(name, salaryPerHour)
    #For each employee, get details from owner and store it in a list
    employees.append(employee)

maxSalary = 0
maxSalaryEmployee = None

for employee in employees:
    #For each employee, ask the no of hrs worked
    hours_worked = float(input("Enter the number of hours worked by {}: ".format(employee.name)))
    #get input from owner
    salary = employee.calculate_salary(hours_worked)
    if salary > maxSalary:
        #Calculate Salary
        maxSalary = salary
        maxSalaryEmployee = employee

#print employeeDetails
print("Employee with the highest salary:")
print("Name: ", maxSalaryEmployee.name)
print("Salary: ", maxSalary)

