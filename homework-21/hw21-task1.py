import json

try:
    with open('data.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: The file 'data.json' does not exist.")
    exit()

class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

class Department:
    def __init__(self, employees):
        self.employees = employees

    def average(self):
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)

    def max_salary(self):
        return max(emp.salary for emp in self.employees)

    def min_salary(self):
        return min(emp.salary for emp in self.employees)

    def positions(self):
        position_count = {}
        for emp in self.employees:
            if emp.position in position_count:
                position_count[emp.position] += 1
            else:
                position_count[emp.position] = 1
        return position_count

employees = []
for emp_data in data['employees']:
    emp = Employee(emp_data['id'], emp_data['name'], emp_data['position'], emp_data['salary'])
    employees.append(emp)

department = Department(employees)

print("Average Salary:", department.average())
print("Max Salary:", department.max_salary())
print("Min Salary:", department.min_salary())
print("Positions:", department.positions())
