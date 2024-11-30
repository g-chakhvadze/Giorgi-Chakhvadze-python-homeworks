import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
        return None

def calculate_avg_salary(data):
    if not data:
        return

    department_salaries = {}
    department_counts = {}

    for employee in data.get('employees', []):
        department = employee.get('department')
        salary = employee.get('salary')

        if department and isinstance(salary, (int, float)):
            if department not in department_salaries:
                department_salaries[department] = 0
                department_counts[department] = 0

            department_salaries[department] += salary
            department_counts[department] += 1

    avg_salaries = {
        department: department_salaries[department] / department_counts[department]
        for department in department_salaries
    }

    return avg_salaries

def write_json_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Average salaries have been written to '{file_path}'.")
    except IOError:
        print(f"Error: Could not write to file '{file_path}'.")

def main():
    input_file = 'data.json'
    output_file = 'avg_salary.json'

    data = read_json_file(input_file)
    if data is None:
        return

    avg_salaries = calculate_avg_salary(data)
    if avg_salaries:
        print("Average salaries per department:")
        for department, avg_salary in avg_salaries.items():
            print(f"{department}: {avg_salary:.2f}")

        write_json_file(output_file, avg_salaries)

if __name__ == "__main__":
    main()
