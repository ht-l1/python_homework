import csv
from datetime import datetime 
import os

import custom_module

# Task 2
def read_employees():
    # Declare an empty dict & empty list
    ee_dict = {}
    ee_list = [] # to store rows
    try:
        with open('../csv/employees.csv', 'r') as file:
            csv_reader = csv.reader(file)
            ee_dict["fields"] = next(csv_reader)
            for row in csv_reader:
                ee_list.append(row)
            ee_dict["rows"] = ee_list
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)
    return ee_dict

employees = read_employees()
print(employees)

# Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

sort_by_last_name()
print(employees)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    return {field: value for field, value in zip(employees["fields"], row) 
            if field != "employee_id"}

example_row = employees["rows"][0]
print(employee_dict(example_row))

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    return {row[employee_id_column]: employee_dict(row) 
            for row in employees["rows"]}

print(all_employees_dict())

# Task 10: Use the os Module
# ran this in terminal: $env:THISVALUE="ABC"
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Creating Your Own Module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("my new secret")
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    def read_file(filename):
        minutes_dict = {}
        rows = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                minutes_dict["fields"] = next(csv_reader)
                for row in csv_reader:
                    rows.append(tuple(row))  
                minutes_dict["rows"] = rows
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            exit(1)
        return minutes_dict

    minutes1 = read_file('../csv/minutes1.csv')
    minutes2 = read_file('../csv/minutes2.csv')
    
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)

# Task 13: Create minutes_set
def create_minutes_set():
    return set(minutes1["rows"]) | set(minutes2["rows"])

minutes_set = create_minutes_set()
print(minutes_set)

# Task 14: Convert to datetime
def create_minutes_list():
    minutes_list = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), 
        list(minutes_set)
    ))
    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    
    formatted_list = list(map(
        lambda x: (x[0], x[1].strftime("%B %d, %Y")), 
        sorted_list
    ))
    
    with open('./minutes.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(minutes1["fields"])
        csv_writer.writerows(formatted_list)
    
    return formatted_list

write_sorted_list()